from graph.state import ResearchState
from agents.llm import get_llm


def report_node(state: ResearchState) -> ResearchState:
    """
    Generates a final structured research report from verified notes.
    """
    notes = state.notes or []
    flags = state.flags or []
    scope = state.research_scope or {}

    if not notes:
        state.final_report = "No sufficient information to generate report."
        return state

    # ---- Build notes section (ROBUST to multiple schemas) ----
    notes_text = ""
    for note in notes:
        heading = note.get("heading", "Findings")
        notes_text += f"## {heading}\n"

        for point in note.get("points", []):
            # Case 1: point is a dict (future-proof)
            if isinstance(point, dict):
                text = point.get("text", "")
                citations = ", ".join(point.get("citations", []))
            # Case 2: point is a plain string (your current synthesis output)
            else:
                text = str(point)
                citations = ""

            if text.strip():
                notes_text += f"- {text}\n"
                if citations:
                    notes_text += f"  **Citations:** {citations}\n"

        notes_text += "\n"

    # ---- Build flags section ----
    flags_text = ""
    if flags:
        flags_text = "## Limitations & Unverified Claims\n"
        for f in flags:
            issue = f.get("issue", "Unspecified issue")
            reason = f.get("reason", "")
            flags_text += f"- {issue}: {reason}\n"

    # ---- Prompt for final report ----
    prompt = f"""
You are a research report writer.

Create a clear, professional academic research report using the information below.
Write in a neutral, formal tone.

Include the following sections:
- Title
- Abstract
- Main Findings
- Limitations
- Conclusion

RESEARCH CONTEXT:
Goal: {scope.get('goal')}
Domain: {scope.get('domain')}
Task: {scope.get('task_type')}

VERIFIED NOTES:
{notes_text}

FLAGS:
{flags_text}
"""

    client = get_llm()
    response = client.models.generate_content(
        model="models/gemini-flash-lite-latest",
        contents=prompt
    )

    state.final_report = response.text
    return state
