import faiss
import numpy as np
from graph.state import ResearchState
from agents.embeddings import embed_texts

def memory_node(state: ResearchState) -> ResearchState:
    """
    Builds a FAISS vector index from retrieved documents.
    """
    texts = []
    metadatas = []

    for doc in state.documents:
        if doc["content"].strip():
            texts.append(doc["content"][:2000])  # cap length
            metadatas.append({
                "title": doc.get("source_title"),
                "url": doc.get("url"),
                "type": doc.get("type")
            })

    if not texts:
        state.embeddings_index = None
        state.embedded_docs = []
        return state

    vectors = embed_texts(texts)
    dim = len(vectors[0])

    index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectors).astype("float32"))

    state.embeddings_index = index
    state.embedded_docs = metadatas
    return state
