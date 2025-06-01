# app.py
import gradio as gr
from admin_ui import admin_panel_ui
from user_ui import user_chat_ui
from config import DEFAULT_DOCUMENTS
from document_processor import load_and_chunk_documents
from vector_db import create_vector_store, vector_store_exists
import os

def initialize_vector_store():
    """Initialize vector store with default documents"""
    if not vector_store_exists():
        print("No documents found...")
        # chunks = load_and_chunk_documents(list(DEFAULT_DOCUMENTS.values()))
        # create_vector_store(chunks)
        # print(f"Created vector store with {len(chunks)} chunks")

def main():
    """Main application"""
    # Initialize vector store
    initialize_vector_store()
    
    # Create Gradio interface
    with gr.Blocks(title="HR Policy Assistant") as app:
        gr.Markdown("# HR Policy Assistant")
        gr.Markdown("Ask questions about policies, procedures, and benefits.")
        gr.Markdown("This application is designed to assist employees with HR-related queries and provide administrative functionalities.")
        
        with gr.Tab("Employee Chat"):
            user_chat_ui()
        
        with gr.Tab("Admin Panel"):
            admin_panel_ui()
    
    app.launch(server_port=8000)

if __name__ == "__main__":
    main()