"""Simple graph utilities."""
from typing import Dict, List
from .state import State


class Graph:
    def __init__(self):
        self.nodes: Dict[str, State] = {}
        self.edges: Dict[str, List[str]] = {}

    def add_node(self, state: State):
        self.nodes[state.id] = state
        self.edges.setdefault(state.id, [])

    def add_edge(self, a: str, b: str):
        self.edges.setdefault(a, []).append(b)
