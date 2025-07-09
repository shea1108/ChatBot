import os
from pathlib import Path
from dotenv import load_dotenv
from llama_index.core import (
    VectorStoreIndex,
    StorageContext,
    SimpleDirectoryReader,
    load_index_from_storage
)
from llama_index.core.settings import Settings
Settings.llm = None
from app.services.embedding_service import get_embedding_model
from app.repository.doc_loader import load_docx_file


env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

DATA_DIR = Path(os.getenv("DATA_DIR", "backend/app/data"))
INDEX_DIR = os.getenv("FAISS_INDEX_PATH", "backend/app/embeddings")

def build_index():
    embed_model = get_embedding_model()
    all_docs = []

    print(f"📂 Đang đọc thư mục: {DATA_DIR}")
    print("📄 Danh sách file trong thư mục:", os.listdir(DATA_DIR))


    if any(f.endswith(".txt") for f in os.listdir(DATA_DIR)):
        txt_docs = SimpleDirectoryReader(str(DATA_DIR), required_exts=[".txt"]).load_data()
        all_docs.extend(txt_docs)

    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".docx"):
            filepath = DATA_DIR / filename
            print(f"📄 Đang load file Word: {filepath}")
            word_docs = load_docx_file(str(filepath))
            all_docs.extend(word_docs)

    if not all_docs:
        print("⚠️ Không có tài liệu nào để index.")
        return

    index = VectorStoreIndex.from_documents(
        all_docs,
        embed_model=embed_model,
        llm=None
    )
    index.storage_context.persist(persist_dir=INDEX_DIR)
    print(f"✅ Index đã được tạo và lưu tại {INDEX_DIR}")

def load_index() -> VectorStoreIndex:
    embed_model = get_embedding_model()
    storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIR)

    return load_index_from_storage(
        storage_context,
        embed_model=embed_model,
        llm=None  
    )
