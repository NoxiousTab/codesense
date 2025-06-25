# 🧠 CodeSense

> AI-powered semantic code search over your own codebase using Tree-sitter + CodeBERT + FAISS + Streamlit

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 🚀 Overview

**CodeSense** lets you perform natural language searches over source code — like "connect to database" or "handle login request" — and retrieve the most semantically relevant functions, not just keyword matches.

Built with:
- **Tree-sitter** for accurate code parsing
- **CodeBERT** for semantic embeddings
- **FAISS** for fast vector search
- **Streamlit** for interactive UI

---

## 📦 Features

✅ Parse source code into meaningful chunks  
✅ Embed code semantically using CodeBERT  
✅ Perform fast vector similarity search  
✅ Interactive Streamlit UI for natural language queries  
✅ Plug-and-play: works on any Python repo  

---

## 📂 Project Structure

codesense/\
├── app/ # Streamlit UI\
├── backend/ # Parser, Embedding, Search engine\
├── data/ # Raw code, processed chunks, embeddings\
├── scripts/ # Manual scripts for testing modules\
└── README.md


---

## 🛠️ Getting Started

### 1. Clone & Setup
```bash
git clone https://github.com/NoxiousTab/codesense.git
cd codesense
python -m venv venv
venv\Scripts\activate    # or source venv/bin/activate on Unix
(Only If Required) pip install tree_sitter-0.20.4-cp310-cp310-win_amd64.whl
pip install -r requirements.txt
python backend/parser/build_language.py # to build my-languages.so
```

### 2. Clone Repos to Analyze
```
python scripts/test_clone.py
```

### 3. Parse Code and extract chunks

```
python scripts/test_extract_chunks.py
```

### 4. Embed Chunks
```
python scripts/test_embed_chunks.py
```

### 5. Launch UI by streamlit
```
streamlit run app/ui.py
```
