import feedparser
from typing import List, Dict
from urllib.parse import quote_plus

def search_arxiv(query: str, max_results: int = 5) -> List[Dict]:
    safe_query = quote_plus(query)  # <-- THIS FIXES IT

    url = (
        "http://export.arxiv.org/api/query?"
        f"search_query=all:{safe_query}&start=0&max_results={max_results}"
    )

    feed = feedparser.parse(url)
    results = []

    for entry in feed.entries:
        results.append({
            "title": entry.title,
            "url": entry.links[0].href,
            "summary": entry.summary,
            "type": "paper"
        })

    return results
