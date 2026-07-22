# 📄 AI Document Assistant

An AI-powered document question-answering application built using **Streamlit**, **Google Gemini**, **Sentence Transformers**, and **FAISS**.

Users can upload a PDF document and ask natural language questions. The application retrieves the most relevant document sections using semantic search and generates accurate answers using Google's Gemini Large Language Model.

---

## 🚀 Features

- 📤 Upload PDF documents
- 📖 Extract text from PDFs
- ✂️ Intelligent text chunking
- 🧠 Semantic search using Sentence Transformers
- ⚡ Fast similarity search with FAISS
- 🤖 AI-generated answers using Google Gemini
- 📊 Document statistics
- 🎯 Relevant context retrieval with similarity scores
- 💻 Interactive Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- Sentence Transformers
- FAISS
- PyPDF
- NumPy

---

## 📂 Project Workflow

1. Upload a PDF document.
2. Extract text from all pages.
3. Split text into smaller chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings in FAISS.
6. Convert the user's question into an embedding.
7. Retrieve the most relevant document chunks.
8. Send only the retrieved context to Gemini.
9. Display an AI-generated answer.

---

## 📁 Project Structure

```
AI-Document-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .streamlit/
│   └── secrets.toml
└── sample_pdfs/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Document-Assistant.git
```

Navigate into the project

```bash
cd AI-Document-Assistant
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🔑 Environment Variables

Create a `.streamlit/secrets.toml` file.

```toml
GEMINI_API_KEY="YOUR_API_KEY"
```

Never upload your API key to GitHub.

---

## 📸 Screenshots

(Add screenshots of your application here.)

---

## 🚧 Future Improvements

- Multi-PDF support
- OCR for scanned documents
- Chat history
- Highlight answer source in PDF
- Support for DOCX and TXT files
- Voice-based document querying
- Deploy on Streamlit Cloud

---

## 📈 Applications

- Research papers
- Academic notes
- Company documents
- Legal documents
- Technical manuals
- Financial reports

---

## 👩‍💻 Author

**Neha Waigokar**

Final Year Electronics & Telecommunication Engineering Student
