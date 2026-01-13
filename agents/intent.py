"""Intent detection agent stub."""
from typing import Dict


class IntentAgent:
    """Simple intent detection stub."""

    def parse(self, text: str) -> Dict[str, float]:
        """Return a dummy intent distribution."""
        # TODO: replace with real model
        return {"intent": 1.0}
