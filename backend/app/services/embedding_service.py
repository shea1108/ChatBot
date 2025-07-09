from dotenv import load_dotenv
from pathlib import Path
from llama_index.embeddings.huggingface import HuggingFaceEmbedding


env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

def get_embedding_model():
    import os
    model_name = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    return HuggingFaceEmbedding(model_name=model_name)
