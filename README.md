# 📄 AI PDF Summarizer

An AI-powered PDF summarization application that extracts text from PDF documents, processes large documents in chunks, and generates a concise final summary using a Large Language Model (LLM).

Built with **Python, Streamlit, PyMuPDF, and Groq**.

---

## 🚀 Features

* 📄 Upload PDF documents
* 🔍 Extract text from PDFs
* 🧹 Clean extracted text
* ✂️ Split large documents into chunks
* 🤖 Summarize each document chunk using an LLM
* 🧠 Combine chunk summaries into one final summary
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
             ┌───────────┴───────────┐
             ▼           ▼           ▼
          Chunk 1     Chunk 2     Chunk N
             │           │           │
             ▼           ▼           ▼
         Summary 1    Summary 2    Summary N
             │           │           │
             └───────────┬───────────┘
                         ▼
                Combine Summaries
                         │
                         ▼
                  Final LLM Summary
                         │
                         ▼
                  Display Result
```

---

## 🧠 Summarization Approach

The application uses a **Map → Reduce** style summarization approach.

### Map

Each document chunk is independently sent to the LLM and summarized.

```text
Chunk 1 → Summary 1
Chunk 2 → Summary 2
Chunk 3 → Summary 3
...
```

### Reduce

The individual summaries are combined and sent to the LLM again to produce one final document summary.

```text
Summary 1
Summary 2
Summary 3
   ↓
Combined Summaries
   ↓
Final AI Summary
```

This allows the application to process documents that are larger than a single LLM input.

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

The document is divided into smaller chunks.

The current chunk size is:

```text
3000 characters
```

### 5. Summarize Each Chunk

Each chunk is sent to the Groq-hosted LLM and summarized independently.

### 6. Combine Chunk Summaries

The individual summaries are combined into a single text representation.

### 7. Generate Final Summary

The combined summaries are sent to the LLM again to create the final document summary.

### 8. Display Result

The final AI-generated summary is displayed in the Streamlit application.

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

### V2 — Full Document Summarization

The current version supports:

* PDF upload
* PDF text extraction
* Text cleaning
* Text chunking
* Multi-chunk processing
* Chunk-level AI summarization
* Combined final summarization
* PDF statistics
* Streamlit interface

### Example

A document containing:

```text
3284 characters
```

is divided into:

```text
2 chunks
```

Each chunk is summarized separately, and the results are then combined to generate the final summary.

---

## 🔮 Future Improvements

Planned improvements include:

* 📌 Summary length selection
* 📚 Multiple summarization styles
* 📄 Page-wise summaries
* 🔎 Keyword extraction
* 📑 Key points and highlights
* 🧠 Improved long-document processing
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

* Artificial Intelligence
* Machine Learning
* NLP
* LLM Applications
* RAG
* Data Science
* UI/UX Design
