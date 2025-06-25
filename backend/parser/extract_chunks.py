import os
import json
from backend.parser.py_parser import extract_code_chunks

def is_python_file(path):
    return path.endswith(".py") and os.path.isfile(path)

def parse_repo(repo_path: str, output_path: str):
    repo_name = os.path.basename(repo_path.rstrip("/\\"))
    output_file = os.path.join(output_path, f"{repo_name}.jsonl")
    os.makedirs(output_path, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as out:
        for root, _, files in os.walk(repo_path):
            for file in files:
                full_path = os.path.join(root, file)
                if is_python_file(full_path):
                    try:
                        chunks = extract_code_chunks(full_path)
                        for chunk in chunks:
                            out.write(json.dumps(chunk) + "\n")
                    except Exception as e:
                        print(f"[!] Failed to parse {full_path}: {e}")
    print(f"[✓] Extracted chunks saved to {output_file}")
