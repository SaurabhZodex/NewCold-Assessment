# llm_utils.py
from langchain_groq import ChatGroq
from groq import Groq
from langchain.prompts import PromptTemplate
from config import LLM_MODEL, LLM_TEMPERATURE, GROQ_API_KEY, TOPK_RELEVANT_CHUNKS
from vector_db import get_vector_store
import json


client = Groq(api_key=GROQ_API_KEY)

def generate_response(query: str) -> tuple:
    """Generate response for user query"""
    # Retrieve relevant chunks
    vector_store = get_vector_store()
    results = vector_store.similarity_search_with_score(query, k=TOPK_RELEVANT_CHUNKS)
    
    # Format context
    context = ""
    sources = []
    for i, (doc, score) in enumerate(results):
        context += f"CHUNK {i+1} ({doc.metadata['source']} - Page {doc.metadata['page']}):\n{doc.page_content}\n\n"
        sources.append(f"{doc.metadata['source']} - Page {doc.metadata['page']}")
    
    # Generate response
    # llm = ChatGroq(
    #     temperature=LLM_TEMPERATURE, 
    #     model_name=LLM_MODEL,
    #     api_key=GROQ_API_KEY
    # )
    
    # prompt = PromptTemplate.from_template(
    #     "You're an HR assistant for new employees. Answer the question using ONLY "
    #     "the provided context. Be concise and factual. If information is missing, "
    #     "say 'I couldn't find relevant policy information'. Always mention the source.\n\n"
    #     "Context:\n{context}\n\nQuestion: {question}\nAnswer:"
    # )
    
    # response = prompt | llm
    # result = response.invoke({"context": context, "question": query})
    
    system_prompt = f"""
    Generate JSON output using ONLY provided context. Follow:
    {{
      "answer": "concise response",
      "sources": [
        {{
          "source": "document_id",
          "page": [int],
          "context": "excerpt"
        }}
      ]
    }}
    Return {{"answer": "I couldn't find relevant policy information", "sources": []}} if context is insufficient.
    """
    
    user_prompt = f"""
    ## Question
    {query}
    
    ## Context
    {context}
    """

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=LLM_TEMPERATURE,
        response_format={"type": "json_object"}
    )
    
    result = json.loads(response.choices[0].message.content)

    # print(json.dumps(result, indent=2))
    
    return result['answer'], result['sources']