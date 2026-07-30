import faiss
import numpy as np
import pickle
import os

INDEX_PATH = "vector_db/faiss.index"
DATA_PATH = "vector_db/data.pkl"

def save_index(vectors, texts):
    dim = len(vectors[0])
    index = faiss.IndexFlatL2(dim)

    index.add(np.array(vectors))

    os.makedirs("vector_db", exist_ok=True)
    faiss.write_index(index, INDEX_PATH)

    with open(DATA_PATH, "wb") as f:
        pickle.dump(texts, f)

def load_index():
    index = faiss.read_index(INDEX_PATH)
    with open(DATA_PATH, "rb") as f:
        texts = pickle.load(f)

    return index, texts

def search(query_vec, k=12):
    index, texts = load_index()
    D, I = index.search(query_vec, k)

    results = []
    for i in I[0]:
        if i < len(texts):
            results.append(texts[i])

    return results