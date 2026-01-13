"""Graph state definitions."""
from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class State:
    id: str
    data: Dict[str, Any]
