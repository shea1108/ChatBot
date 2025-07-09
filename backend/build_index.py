from pathlib import Path
from dotenv import load_dotenv
from app.repository.vector_store import build_index

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

if __name__ == "__main__":
    print("🔧 Đang tạo index từ tài liệu người dùng...")
    build_index()
    print("✅ Đã hoàn tất xây dựng LlamaIndex.")
