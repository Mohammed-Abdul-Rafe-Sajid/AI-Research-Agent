from typing import List, Dict, Any
from pydantic import BaseModel

class ResearchState(BaseModel):
    user_query: str = ""
    research_scope: Dict[str, Any] = {}
    plan: List[str] = []
    sources: List[Dict[str, Any]] = []
    documents: List[Dict[str, Any]] = []
    notes: List[Dict[str, Any]] = []
    flags: List[Dict[str, Any]] = []
    confidence_score: float = 0.0
    final_report: str = ""
