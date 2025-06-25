import os
import ast
import json
from tree_sitter import Language, Parser

LIB_PATH = os.path.abspath("build/my-languages.so")
PY_LANGUAGE = Language(LIB_PATH, "python")

parser = Parser()
parser.set_language(PY_LANGUAGE)

def extract_code_chunks(filepath: str) -> list[dict]:
    with open(filepath, "r", encoding="utf-8") as f:
        source_code = f.read()
    
    tree = parser.parse(bytes(source_code, "utf8"))
    root = tree.root_node

    results = []
    for node in root.children:
        if node.type in ("function_definition", "class_definition"):
            start = node.start_byte
            end = node.end_byte
            chunk = source_code[start:end].strip()

            results.append({
                "type": node.type,
                "start_line": node.start_point[0],
                "end_line": node.end_point[0],
                "code": chunk,
                "filepath": filepath
            })

    return results
