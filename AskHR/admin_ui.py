# admin_ui.py
import gradio as gr
from document_processor import load_and_chunk_documents
from vector_db import create_vector_store, vector_store_exists
from config import ALLOWED_EXTENSIONS

def admin_panel_ui():
    """Create Gradio UI for admin panel"""
    with gr.Blocks() as panel:
        gr.Markdown("## HR Document Management")
        
        with gr.Row():
            file_input = gr.File(
                file_count="multiple",
                file_types=ALLOWED_EXTENSIONS,
                label="Upload HR Documents"
            )
            process_btn = gr.Button("Process Documents", variant="primary")
        
        status_output = gr.Textbox(label="Processing Status", interactive=False)
        
        process_btn.click(
            fn=process_documents,
            inputs=file_input,
            outputs=status_output
        )
    
    return panel

def process_documents(files: list) -> str:
    """Process uploaded documents and store in vector DB"""
    try:
        # Get file paths
        file_paths = [file.name for file in files]
        
        # Process documents
        chunks = load_and_chunk_documents(file_paths)
        create_vector_store(chunks)
        
        return f"Successfully Processed {len(chunks)} chunks from {len(file_paths)} documents!"
    except Exception as e:
        return f"Failed Error: {str(e)}"