# src/rag/embedder.py
from sentence_transformers import SentenceTransformer
import pandas as pd
import faiss
import numpy as np
import pickle

def build_vector_store(csv_path: str, output_path: str = "data/faiss_store"):
    df = pd.read_csv(csv_path)
    df["text"] = df["title"].fillna("") + ". " + df["analysis"].fillna("")

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(df["text"].tolist(), show_progress_bar=True)

    index = faiss.IndexFlatL2(embeddings[0].shape[0])
    index.add(np.array(embeddings))

    faiss.write_index(index, f"{output_path}.index")

    with open(f"{output_path}.pkl", "wb") as f:
        pickle.dump(df, f)
