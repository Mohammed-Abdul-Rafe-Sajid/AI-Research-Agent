"""Planner agent stub."""
from typing import List, Dict


class Planner:
    """Create simple plans from intents."""

    def plan(self, intent: Dict[str, float]) -> List[str]:
        """Return a list of steps for a given intent."""
        # TODO: implement planning logic
        return ["analyze", "retrieve", "synthesize", "verify", "report"]
