from graph.state import ResearchState
from agents.llm import get_llm
import json

def verification_node(state: ResearchState) -> ResearchState:
    """
    Verifies synthesized notes against retrieved sources and attaches citations.
    """
    if not state.notes or not state.embedded_docs:
        state.flags = []
        return state

    # Build source list
    sources_text = "\n".join(
        f"- {doc.get('title')} ({doc.get('url')})"
        for doc in state.embedded_docs
    )

    prompt = f"""
You are a research verification agent.

Given the NOTES and SOURCES below:
1. Verify whether each note is supported by the sources
2. Attach citations (paper titles or URLs)
3. Flag unsupported or weak claims

Return STRICT JSON:
{{
  "verified_notes": [
    {{
      "heading": "...",
      "points": [
        {{
          "text": "...",
          "citations": ["...", "..."]
        }}
      ]
    }}
  ],
  "flags": [
    {{
      "issue": "...",
      "reason": "..."
    }}
  ]
}}

NOTES:
{json.dumps(state.notes, indent=2)}

SOURCES:
{sources_text}
"""

    client = get_llm()
    response = client.models.generate_content(
        model="models/gemini-flash-lite-latest",
        contents=prompt
    )

    # Defensive parsing
    try:
        data = json.loads(response.text)
        state.notes = data.get("verified_notes", [])
        state.flags = data.get("flags", [])
    except Exception:
        state.flags = [{"issue": "Verification failed", "reason": "Invalid model output"}]

    return state
