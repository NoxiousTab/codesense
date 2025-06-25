import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.parser.extract_chunks import parse_repo

if __name__ == "__main__":
    repos = [
        "privacy_vault",
        "practice_judge",
        "Python"
    ]

    for repo in repos:
        path = f"data/raw_code/{repo}"
        parse_repo(path, "data/processed_chunks")
