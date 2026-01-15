import json
from typing import Any, Dict

def safe_json_loads(text: str, fallback: Dict[str, Any]):
    try:
        return json.loads(text)
    except Exception:
        return fallback
