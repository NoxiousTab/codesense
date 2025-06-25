import os, json
import faiss
import numpy as np

from backend.embeddings.hf_embedder import get_embedding

class CodeSearchEngine:
    def __init__(self, embedding_dir: str):
        self.index = None
        self.chunks = []
        self.load_embeddings(embedding_dir)

    def load_embeddings(self, embedding_dir: str):
        all_vectors = []
        for fname in os.listdir(embedding_dir):
            if not fname.endswith(".jsonl"):
                continue

            with open(os.path.join(embedding_dir, fname), "r", encoding="utf-8") as f:
                for line in f:
                    obj = json.loads(line)
                    self.chunks.append(obj)
                    all_vectors.append(obj["embedding"])

        self.index = faiss.IndexFlatL2(len(all_vectors[0]))
        self.index.add(np.array(all_vectors).astype("float32"))

    def search(self, query: str, top_k: int = 5):
        query_vec = np.array([get_embedding(query)]).astype("float32")
        D, I = self.index.search(query_vec, top_k)
        return [self.chunks[i] for i in I[0]]
