import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.embeddings.embed_chunks import embed_chunks

if __name__ == "__main__":
    embed_chunks("data/processed_chunks", "data/embeddings")
