import numpy as np
from typing import List, Dict
from agents.embeddings import embed_texts

def search_memory(query: str, index, metadatas: List[Dict], k: int = 5):
    """
    Semantic search over FAISS index.
    Returns top-k metadata entries.
    """
    query_vec = embed_texts([query])[0]
    query_vec = np.array([query_vec]).astype("float32")

    distances, indices = index.search(query_vec, k)

    results = []
    for idx in indices[0]:
        if idx < len(metadatas):
            results.append(metadatas[idx])
    return results
