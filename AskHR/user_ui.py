# user_ui.py
import gradio as gr
from llm_utils import generate_response

def user_chat_ui():
    """Create Gradio UI for user chat"""
    with gr.Blocks() as chat:
        gr.Markdown("## HR Assistant - Ask Policy Questions")
        
        chatbot = gr.Chatbot(height=400)
        msg = gr.Textbox(label="Your Question")
        clear = gr.Button("Clear Chat")
        
        def respond(message, chat_history):
            response, sources = generate_response(message)
            sources_text = "\nSources: " + str(sources) if len(sources)!=0 else ""
            chat_history.append((message, response + sources_text))
            return "", chat_history
        
        msg.submit(
            fn=respond,
            inputs=[msg, chatbot],
            outputs=[msg, chatbot]
        )
        clear.click(lambda: None, None, chatbot, queue=False)
    
    return chat

# {
#   "answer": "The company has various types of leaves including Annual Leave (18 days), Sick Leave (12 days), Casual Leave (6 days), Maternity Leave (26 weeks), and Paternity Leave (10 days). Leaves must be applied at least 3 days in advance on the HRMS platform.",
#   "sources": [
#     {
#       "source": "Leave_Policy",
#       "page": 1,
#       "context": "2. Types of Leaves Employees are entitled to various types of leaves including: Annual Leave (18 days), Sick Leave (12 days), and Casual Leave (6 days)."
#     },
#     {
#       "source": "Leave_Policy",
#       "page": 1,
#       "context": "3. Maternity & Paternity Leave Female employees are entitled to 26 weeks of maternity leave. Male employees can avail 10 days of paternity leave."
#     },
#     {
#       "source": "Leave_Policy",
#       "page": 1,
#       "context": "5. Leave Application Process Leaves must be applied at least 3 days in advance on the HRMS platform, except in case of emergencies."
#     }
#   ]
# }