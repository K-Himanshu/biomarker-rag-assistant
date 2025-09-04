from langchain_community.vectorstores import FAISS 
from langchain_community.embeddings import HuggingFaceEmbeddings

def build_faiss_retriever(docs, model_name="sentence-transformers/all-MiniLM-L6-v2", k=3):
    """
    Build a FAISS retriever directly from documents.
    Default embedding model = all-MiniLM-L6-v2 (fast + free).
    """
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    db = FAISS.from_documents(docs, embeddings)
    retriever = db.as_retriever(search_kwargs={"k": k})
    return retriever