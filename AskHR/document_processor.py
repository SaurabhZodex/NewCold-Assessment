# document_processor.py
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP

def load_and_chunk_documents(file_paths: list) -> list:
    """Load and split PDF documents into chunks"""
    documents = []
    for path in file_paths:
        try:
            loader = PyPDFLoader(path)
            pages = loader.load()
            for page in pages:
                doc_name = path.split("/")[-1].replace('.pdf', '')
                page.metadata["source"] = doc_name
                page.metadata["page"] = page.metadata.get("page", 0) + 1
            documents.extend(pages)
        except Exception as e:
            print(f"Error loading {path}: {str(e)}")
            raise
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return text_splitter.split_documents(documents)