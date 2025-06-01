# vector_db.py
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import EMBEDDING_MODEL, PERSIST_DIR


embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

def create_vector_store(chunks: list) -> Chroma:
    """Create Chroma vector store from document chunks"""
    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=PERSIST_DIR
    )

def get_vector_store() -> Chroma:
    """Get existing Chroma vector store"""
    return Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embeddings
    )

def vector_store_exists() -> bool:
    """Check if vector store exists"""
    import os
    return os.path.exists(PERSIST_DIR)