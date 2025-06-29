import faiss
import os
import pickle
from backend.Service.embedder import Embedder


class VectorStore:
    def __init__(self, data_path="data/my_notes.txt", index_dir="faiss_store"):
        self.embedder = Embedder()
        self.data_path = data_path
        self.index_dir = index_dir
        self.index_path = os.path.join(index_dir, "index.faiss")
        self.chunk_path = os.path.join(index_dir, "chunks.pkl")

    def build_index(self, chunk_size=300):
        with open(self.data_path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        chunks = [raw_text[i:i+chunk_size] for i in range(0, len(raw_text), chunk_size)]
        embeddings = self.embedder.embed(chunks)

        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(embeddings)

        os.makedirs(self.index_dir, exist_ok=True)
        faiss.write_index(index, self.index_path)

        with open(self.chunk_path, "wb") as f:
            pickle.dump(chunks, f)

        print("FAISS index đã lưu thành công.")

    def search(self, query, top_k=3):
        index = faiss.read_index(self.index_path)
        with open(self.chunk_path, "rb") as f:
            chunks = pickle.load(f)

        q_emb = self.embedder.embed([query])
        _, indices = index.search(q_emb, top_k)
        return [chunks[i] for i in indices[0]]