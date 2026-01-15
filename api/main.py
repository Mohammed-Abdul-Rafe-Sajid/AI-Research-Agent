import argparse
from graph.graph import build_graph
from graph.state import ResearchState


def run(query: str):
    graph = build_graph()

    state = ResearchState(
        user_query=query,
        research_scope={},
        plan=[],
        sources=[],
        documents=[],
        notes=[],
        flags=[],
        final_report=""
    )

    final_state = graph.invoke(state)

    print("\n" + "=" * 80)
    print("FINAL RESEARCH REPORT\n")
    print(final_state.get("final_report", "No report generated."))
    print("=" * 80)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Agentic AI Research Assistant (LangGraph + Gemini)"
    )
    parser.add_argument(
        "--query",
        type=str,
        required=True,
        help="Research question to investigate"
    )

    args = parser.parse_args()
    run(args.query)
