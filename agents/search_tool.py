import os
import time
from typing import List, Dict, Optional
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")  # optional, for real searches

class SearchTool:
    """
    Minimal pluggable search tool. Default behavior:
     - If SERPAPI_KEY present, use SerpAPI.
     - Otherwise, operate in mock mode.
    """

    def __init__(self, num_results: int = 5):
        self.num_results = num_results
        self.mode = "serpapi" if SERPAPI_KEY else "mock"

    def search(self, query: str) -> List[Dict]:
        if self.mode == "serpapi":
            return self._serpapi_search(query)
        else:
            return self._mock_search(query)

    def _serpapi_search(self, query: str) -> List[Dict]:
        # lightweight SerpAPI implementation (needs serpapi package and key)
        from serpapi import GoogleSearch  # pip install google-search-results
        params = {
            "engine": "google_scholar",
            "q": query,
            "api_key": SERPAPI_KEY,
            "num": self.num_results
        }
        results = []
        try:
            search = GoogleSearch(params)
            res = search.get_dict()
            items = res.get("organic_results") or []
            for item in items[: self.num_results]:
                results.append({
                    "title": item.get("title"),
                    "url": item.get("link") or item.get("url"),
                    "snippet": item.get("snippet") or "",
                    "type": "paper" if ".pdf" in (item.get("link") or "") else "article"
                })
                time.sleep(0.1)
        except Exception:
            return self._mock_search(query)
        return results

    def _mock_search(self, query: str) -> List[Dict]:
        # deterministic small mock results for dev/testing
        return [
            {
                "title": f"Mock paper about {query} - 2024",
                "url": "https://arxiv.org/pdf/0000.00000.pdf",
                "snippet": f"Mock snippet for {query}",
                "type": "paper"
            },
            {
                "title": f"Overview article on {query}",
                "url": "https://example.com/article-about",
                "snippet": f"Example article snippet for {query}",
                "type": "article"
            }
        ]
