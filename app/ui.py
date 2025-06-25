import streamlit as st
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.search.search_engine import CodeSearchEngine


@st.cache_resource
def load_engine():
    return CodeSearchEngine("data/embeddings")

engine = load_engine()

st.set_page_config(page_title="CodeSense", layout="wide")
st.title("🔍 CodeSense — Semantic Code Search")

query = st.text_input("Search your codebase...", placeholder="e.g., connect to database, handle API request")

if query:
    with st.spinner("Searching..."):
        results = engine.search(query, top_k=5)

    for i, r in enumerate(results, 1):
        st.markdown(f"**[{i}] `{r['type']}`** — `{r['filepath']} ({r['start_line']}–{r['end_line']})`")
        st.code(r["code"], language="python")
