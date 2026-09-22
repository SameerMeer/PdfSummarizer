# 📄 AI PDF Summarizer

An AI-powered PDF summarization application that extracts text from PDF documents and generates concise summaries using a Large Language Model (LLM).

Built with **Python, Streamlit, PyMuPDF, and Groq**.

---

## 🚀 Features

* 📄 Upload PDF documents
* 🔍 Extract text from PDFs
* 🧹 Clean extracted text
* ✂️ Split large documents into chunks
* 🤖 Generate AI-powered summaries
* 📊 Display PDF statistics
* ⚡ Simple and interactive Streamlit interface

---

## 🏗️ Project Architecture

```text
             PDF Upload
                  │
                  ▼
          PyMuPDF Extraction
                  │
                  ▼
            Text Cleaning
                  │
                  ▼
              Chunking
                  │
                  ▼
             Groq LLM
                  │
                  ▼
           AI Generated Summary
```

---

## 🛠️ Tech Stack

| Technology    | Purpose                         |
| ------------- | ------------------------------- |
| Python        | Core programming language       |
| Streamlit     | Web application interface       |
| PyMuPDF       | PDF text extraction             |
| Groq          | LLM API                         |
| python-dotenv | Environment variable management |

---

## 📁 Project Structure

```text
PdfSummarizer/
│
├── app.py
├── summarizer.py
├── pdf_processor.py
├── chunker.py
├── test_groq.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

### 1. Upload PDF

The user uploads a PDF through the Streamlit interface.

### 2. Extract Text

PyMuPDF reads the PDF and extracts text from each page.

### 3. Clean Text

The extracted text is cleaned by removing unnecessary whitespace and formatting.

### 4. Chunk Text

Large documents are divided into smaller text chunks so they can be processed by the language model.

### 5. Generate Summary

The text is sent to a Groq-hosted LLM with a summarization prompt.

### 6. Display Result

The generated summary is displayed in the Streamlit application.

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/SameerMeer/PdfSummarizer.git
```

Move into the project directory:

```bash
cd PdfSummarizer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file in the project directory:

```text
GROQ_API_KEY=your_groq_api_key
```

**Never upload your `.env` file or API key to GitHub.**

The project already includes `.env` in `.gitignore`.

---

## ▶️ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📊 Current Version

### V1

The current version supports:

* PDF upload
* PDF text extraction
* Text cleaning
* Text chunking
* AI summarization
* PDF statistics

---

## 🔮 Future Improvements

Planned improvements include:

* 📝 Full-document summarization for large PDFs
* 📌 Summary length selection
* 📚 Multiple summarization styles
* 📄 Page-wise summaries
* 🔎 Keyword extraction
* 📑 Key points and highlights
* 🧠 Better long-document processing
* 💬 Chat with PDF
* 📥 Download generated summaries
* 🔐 Improved API and error handling
* 👁️ OCR support for scanned PDFs

---

## 🎯 Learning Goals

This project is part of my journey toward learning:

```text
Python
   ↓
NLP
   ↓
LLMs
   ↓
Embeddings
   ↓
RAG
   ↓
AI Applications
```

The project focuses on understanding how an AI application can process real-world documents and use an LLM to generate useful information.

---

## 👨‍💻 Author

**Sameer Meer**

B.Tech Computer Science & Engineering

Interested in:

* Artificial
