"""Retrieval agent stub."""
from typing import List


class RetrievalAgent:
    """Retrieve data or documents relevant to a query."""

    def retrieve(self, query: str, k: int = 5) -> List[str]:
        """Return a list of document ids or text snippets."""
        # TODO: hook up to vector DB or search index
        return [f"doc_{i}" for i in range(k)]
