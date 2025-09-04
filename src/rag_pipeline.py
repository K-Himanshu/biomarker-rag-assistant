# src/rag_pipeline.py
from src.loader import load_and_split_pdf
from src.embedder import build_faiss_retriever   # ✅ FIXED
from src.utils import pretty_print

def build_pipeline(pdf_path: str):
    # Step 1: Load & split PDF
    chunks = load_and_split_pdf(pdf_path)

    # Step 2 + 3: Build FAISS index & return retriever
    retriever = build_faiss_retriever(chunks)

    return retriever

def ask_question(retriever, question: str):
    """Queries the retriever for an answer."""
    docs = retriever.get_relevant_documents(question)
    pretty_print(docs)
    return docs

if __name__ == "__main__":
    retriever = build_pipeline(
        r"C:\Users\write\OneDrive\Desktop\biomarker-rag-assistant-project\biomarker-rag-assistant\data\bimarker-doc.pdf"
    )
    ask_question(retriever, "What biomarkers are discussed?")