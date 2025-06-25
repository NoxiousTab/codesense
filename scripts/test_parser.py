import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.parser.py_parser import extract_code_chunks

filepath = "data/raw_code/privacy_vault/app.py"
chunks = extract_code_chunks(filepath)

for c in chunks:
    print(f"\n[{c['type']}] {c['filepath']} ({c['start_line']}–{c['end_line']})")
    print(c["code"])
