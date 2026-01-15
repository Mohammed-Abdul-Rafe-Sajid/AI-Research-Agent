from graph.state import ResearchState
from agents.llm import get_llm
import json
from agents.utils import safe_json_loads


def intent_node(state: ResearchState) -> ResearchState:
    """
    Intent Analyzer Agent
    - Reads: user_query
    - Writes: research_scope
    """

    client = get_llm()

    prompt = f"""
You are an Intent Analyzer Agent in a research assistant system.

Analyze the user query and extract:
- goal
- domain
- task_type (survey, comparison, summary, critique)
- depth (overview or deep dive)

User Query:
"{state.user_query}"

Return ONLY valid JSON in this format:
{{
  "goal": "",
  "domain": "",
  "task_type": "",
  "depth": ""
}}
"""

    response = client.models.generate_content(
    model="models/gemini-flash-lite-latest",
    contents=prompt
)
    
    raw = response.text or ""

    scope = safe_json_loads(
    raw,
    fallback={
        "goal": state.user_query,
        "domain": "computer science research",
        "task_type": "analysis",
        "depth": "overview"
    }
)

    state.research_scope = scope

    return state
