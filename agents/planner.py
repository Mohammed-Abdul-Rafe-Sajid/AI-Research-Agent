from graph.state import ResearchState
from agents.llm import get_llm
import json
from agents.utils import safe_json_loads

def planner_node(state: ResearchState) -> ResearchState:
    """
    Research Planner Agent
    - Reads: research_scope
    - Writes: plan
    """

    client = get_llm()

    prompt = f"""
You are a Research Planner Agent.

Based on the research scope below, create a clear, ordered research plan.
Each step must be actionable and atomic.

Research Scope:
{state.research_scope}

Return ONLY valid JSON:
{{
  "plan": [
    "step 1",
    "step 2",
    "step 3"
  ]
}}
"""

    response = client.models.generate_content(
    model="models/gemini-flash-lite-latest",
    contents=prompt
)
    

    raw = response.text or ""

    plan_data = safe_json_loads(
        raw,
        fallback={
        "plan": [
            "Search recent research papers",
            "Extract CNN and ViT architectures",
            "Compare performance metrics",
            "Analyze strengths and limitations",
            "Summarize findings"
        ]
    }
)

    state.plan = plan_data["plan"]
    return state
