from graph.state import ResearchState
from agents.llm import get_llm
from agents.memory_search import search_memory
import json

def synthesis_node(state: ResearchState) -> ResearchState:
    """
    Uses vector memory to synthesize research insights.
    """
    # Guard: if no memory, return empty notes
    if not state.embeddings_index or not state.embedded_docs:
        state.notes = []
        return state

    # Build a focused query from scope
    scope = state.research_scope
    query = (
        f"{scope.get('goal', '')}. "
        f"Domain: {scope.get('domain', '')}. "
        f"Task: {scope.get('task_type', '')}."
    )

    # Retrieve relevant docs from memory
    top_sources = search_memory(
        query=query,
        index=state.embeddings_index,
        metadatas=state.embedded_docs,
        k=5
    )

    # Build context for LLM
    context = "\n".join(
        f"- {s.get('title')} ({s.get('url')})"
        for s in top_sources
    )

    prompt = f"""
You are a research assistant.

Using ONLY the sources below, produce a structured synthesis with:
- Key comparisons
- Strengths
- Weaknesses
- Notable trends

Return STRICT JSON with this format:
{{
  "notes": [
    {{"heading": "...", "points": ["...", "..."]}}
  ]
}}

SOURCES:
{context}
"""

    client = get_llm()
    response = client.models.generate_content(
        model="models/gemini-flash-lite-latest",
        contents=prompt
    )

    # Defensive JSON parsing
    try:
        data = json.loads(response.text)
        state.notes = data.get("notes", [])
    except Exception:
        state.notes = []

    return state
