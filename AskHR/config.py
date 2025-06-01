# config.py
import os
from dotenv import load_dotenv

# Document processing
CHUNK_SIZE = 200
CHUNK_OVERLAP = 20
ALLOWED_EXTENSIONS = [".pdf"]

# Embedding model
EMBEDDING_MODEL = "BAAI/llm-embedder"

# Vector database
PERSIST_DIR = "../chroma_db"
TOPK_RELEVANT_CHUNKS = 2

# LLM configuration
LLM_MODEL = "llama-3.3-70b-versatile"
LLM_TEMPERATURE = 0

# Load the API key from .env file
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# print(f"GROQ_API_KEY: {GROQ_API_KEY}")

# Default documents
DEFAULT_DOCUMENTS = {
    "Leave_Policy": "Data/Leave_Policy.pdf",
    "Performance_Appraisal_Policy": "Data/Performance_Appraisal_Policy.pdf",
    "Travel_Reimbursement_Policy": "Data/Travel_and_Reimbursement_Policy.pdf"
}