from graph.state import ResearchState
from agents.llm import get_llm
from agents.memory_search import search_memory
import json
import re


def synthesis_node(state: ResearchState) -> ResearchState:
    """
    Uses vector memory (FAISS) to synthesize grounded research insights.
    """

    # Guard: memory must exist
    if not state.embeddings_index or not state.embedded_docs:
        state.notes = []
        return state

    # Build a focused semantic query
    scope = state.research_scope
    query = (
        f"{scope.get('goal', '')}. "
        f"Domain: {scope.get('domain', '')}. "
        f"Task: {scope.get('task_type', '')}."
    )

    # Retrieve relevant documents from vector memory
    top_sources = search_memory(
        query=query,
        index=state.embeddings_index,
        metadatas=state.embedded_docs,
        k=5
    )

    if not top_sources:
        state.notes = []
        return state

    # Build grounded context (REAL content, not metadata)
    context = "\n\n".join(
        f"TITLE: {s.get('title')}\n"
        f"SOURCE: {s.get('url')}\n"
        f"CONTENT:\n{s.get('content')}"
        for s in top_sources
    )

    prompt = f"""
You are a research assistant.

Using ONLY the sources below, produce a structured synthesis.

You MUST include:
- At least 2 comparison points
- At least 2 strengths
- At least 2 limitations

If evidence is weak or indirect, state that clearly.

Return STRICT JSON ONLY in the following format:
{{
  "notes": [
    {{
      "heading": "...",
      "points": ["...", "..."]
    }}
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

    # ---- Robust JSON extraction (CRITICAL FIX) ----
    raw = response.text.strip()

    # Remove markdown code fences if present
    raw = re.sub(r"^```(?:json)?", "", raw)
    raw = re.sub(r"```$", "", raw)
    raw = raw.strip()

    try:
        data = json.loads(raw)
        state.notes = data.get("notes", [])
    except Exception:
        state.notes = []

    return state
