import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.search.search_engine import CodeSearchEngine

if __name__ == "__main__":
    engine = CodeSearchEngine("data/embeddings")

    while True:
        query = input("🔍 Search code for: ")
        results = engine.search(query, top_k=5)

        print("\n--- Top Results ---")
        for i, r in enumerate(results, 1):
            print(f"\n[{i}] {r['type']} @ {r['filepath']} ({r['start_line']}-{r['end_line']})")
            print(r["code"])
            print("-" * 40)
