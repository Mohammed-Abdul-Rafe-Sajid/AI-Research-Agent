from langgraph.graph import StateGraph, END
from graph.state import ResearchState

from agents.intent import intent_node
from agents.planner import planner_node
from agents.retrieval import retrieval_node
from agents.memory import memory_node
from agents.synthesis import synthesis_node
from agents.verification import verification_node
from agents.report import report_node

def build_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("intent", intent_node)
    graph.add_node("planner", planner_node)
    graph.add_node("retrieval", retrieval_node)
    graph.add_node("memory", memory_node)
    graph.add_node("synthesis", synthesis_node)
    graph.add_node("verification", verification_node)
    graph.add_node("report", report_node)

    graph.set_entry_point("intent")
    

    # graph.add_edge("intent", "planner")
    # graph.add_edge("planner", "retrieval")
    # graph.add_edge("retrieval", "memory")
    # graph.add_edge("memory", "synthesis")
    # graph.add_edge("synthesis", END)

    graph.add_edge("intent", "planner")
    graph.add_edge("planner", "retrieval")
    graph.add_edge("retrieval", "memory")
    graph.add_edge("memory", "synthesis")
    graph.add_edge("synthesis", "verification")
    graph.add_edge("verification", "report")
    graph.add_edge("report", END)

    return graph.compile()
