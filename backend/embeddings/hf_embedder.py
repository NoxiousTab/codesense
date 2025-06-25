import os
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModel
import torch

load_dotenv()
MODEL_NAME = "BAAI/bge-small-en"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModel.from_pretrained(MODEL_NAME)

def get_embedding(text: str) -> list[float]:
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state[:, 0, :]  # CLS token
        return embeddings[0].tolist()
