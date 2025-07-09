from app.repository.vector_store import load_index
from app.models.llama_model import generate_with_ollama

def generate_response(question: str) -> str:
    index = load_index()
    query_engine = index.as_query_engine(similarity_top_k=3, llm=None)

    response = query_engine.query(question)
    source_texts = [node.get_content() for node in response.source_nodes]
    context = "\n\n".join(source_texts) + "\n" + str(response)

    prompt = f"""<|begin_of_text|>
[System]: Bạn là trợ lý AI thân thiện, hãy trả lời dựa vào ngữ cảnh bên dưới.
[Context]: 
{context}

[User]: {question}
[Assistant]:"""

    return generate_with_ollama(prompt).strip()