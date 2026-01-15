from graph.state import ResearchState
from agents.arxiv_tool import search_arxiv
from agents.pdf_reader import download_pdf, extract_pdf_text

def retrieval_node(state: ResearchState) -> ResearchState:
    sources = []
    documents = []

    for step in state.plan:
        results = search_arxiv(step, max_results=3)

        for r in results:
            sources.append(r)

            pdf_url = r["url"].replace("abs", "pdf") + ".pdf"
            pdf_path = download_pdf(pdf_url)

            content = ""
            if pdf_path:
                content = extract_pdf_text(pdf_path)

            documents.append({
                "source_title": r["title"],
                "url": pdf_url,
                "content": content[:20000],
                "type": "paper"
            })

    state.sources = sources
    state.documents = documents
    return state
