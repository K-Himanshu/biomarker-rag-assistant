
# 🔬 Biomarker RAG Assistant

*A Retrieval-Augmented Generation (RAG) project for querying biomedical literature (Module 1 – Agentic AI Developer Certification)*

---

## ✨ Overview

This project implements a **RAG-powered assistant** that helps researchers query biomedical PDFs, with a focus on **biomarker–cancer relationships**.
It combines a **vector database (FAISS)** with a **lightweight LLM (Flan-T5)** to provide evidence-grounded answers from scientific texts.

---

## 🎯 Objectives

* Build a working **RAG pipeline** using only free/open-source tools.
* Enable **natural language queries** on biomarker-related literature.
* Showcase an **end-to-end reproducible pipeline** for Module 1 submission.

---

## 🏗️ Architecture

**Pipeline Components:**

1. **PDF Loader** – Extracts text using `pypdf`.
2. **Chunking** – Splits into \~1000-token chunks using `RecursiveCharacterTextSplitter`.
3. **Embeddings** – Biomedical embeddings via `sentence-transformers/all-MiniLM-L6-v2` (fast + free).
4. **Vector DB** – Stores embeddings in **FAISS**.
5. **LLM** – `google/flan-t5-base` for Q\&A.
6. **RAG Workflow** – Retrieve relevant chunks → LLM generates answers.

---

## 📂 Project Structure

```bash
biomarker-rag-assistant/
│── data/                        # Sample PDFs (do not commit large PDFs to GitHub)
│   └── sample.pdf
│
│── notebooks/                   # Jupyter/Colab experiments
│   └── rag_experiments.ipynb
│
│── src/                         # Core Python source code
│   ├── __init__.py
│   ├── loader.py                # PDF loading + text splitting
│   ├── embedder.py              # Embeddings + FAISS vector store
│   ├── rag_pipeline.py          # Main RAG pipeline (ask_question, etc.)
│   └── utils.py                 # Helper functions
│
│── requirements.txt             # Python dependencies
│── README.md                    # Project description & usage
│── .gitignore                   # Ignore venv, cache, and large files
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/biomarker-rag-assistant.git
cd biomarker-rag-assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

* **Windows (PowerShell / VS Code):**

```bash
venv\Scripts\activate
```

* **Mac/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Example Notebook

```bash
jupyter notebook notebooks/rag_experiments.ipynb
```

### 6. Deactivate Environment (when done)

