import os, json
from backend.embeddings.hf_embedder import get_embedding

def embed_chunks(input_path: str, output_path: str):
    os.makedirs(output_path, exist_ok=True)
    files = [f for f in os.listdir(input_path) if f.endswith(".jsonl")]

    for fname in files:
        in_file = os.path.join(input_path, fname)
        out_file = os.path.join(output_path, fname)

        with open(in_file, "r", encoding="utf-8") as f_in, open(out_file, "w", encoding="utf-8") as f_out:
            for line in f_in:
                obj = json.loads(line)
                emb = get_embedding(obj["code"])
                obj["embedding"] = emb
                f_out.write(json.dumps(obj) + "\n")

        print(f"[✓] Embedded {fname}")
