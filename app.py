import streamlit as st
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import google.generativeai as genai
import os

# ==============================
# Configure Gemini API
# ==============================

# Replace with your Gemini API key
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# ==============================
# Streamlit UI
# ==============================

st.set_page_config(page_title="AI Document Assistant", page_icon="📄")

st.title("📄 AI Document Assistant")
st.write("Upload a PDF and ask questions about its contents.")

# ==============================
# Load Embedding Model (Cached)
# ==============================

@st.cache_resource
def load_embedding_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

embed_model = load_embedding_model()

# ==============================
# Upload PDF
# ==============================

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:

    # Read PDF
    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    if not text.strip():
        st.error("No readable text found in the uploaded PDF.")
        st.stop()

    st.success("PDF uploaded successfully!")

    # ==============================
    # Split into chunks
    # ==============================

    chunk_size = 500

    chunks = [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]

    # ==============================
    # Create Embeddings
    # ==============================

    with st.spinner("Creating embeddings..."):

        embeddings = embed_model.encode(
            chunks,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

    # ==============================
    # Build FAISS Index
    # ==============================

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)

    index.add(embeddings.astype(np.float32))

    st.success(f"Indexed {len(chunks)} text chunks.")

    # ==============================
    # Ask Question
    # ==============================

    question = st.text_input("Ask a question from the PDF")

    if question:

        with st.spinner("Searching document..."):

            query_embedding = embed_model.encode(
                [question],
                convert_to_numpy=True,
                normalize_embeddings=True
            )

            distances, indices = index.search(
                query_embedding.astype(np.float32),
                k=3
            )

            context = "\n\n".join(
                [chunks[i] for i in indices[0]]
            )

        prompt = f"""
You are an AI assistant.

Use ONLY the information given in the context.

If the answer is not found in the context, reply exactly:

"I couldn't find the answer in the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""

        try:

            with st.spinner("Generating answer..."):

                response = model.generate_content(prompt)

            st.subheader("AI Answer")

            st.write(response.text)

            with st.expander("Retrieved Context"):

                st.write(context)

        except Exception as e:

            st.error("Error while generating response.")

            st.write(str(e))