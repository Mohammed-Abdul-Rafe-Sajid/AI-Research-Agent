from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class ResearchState(BaseModel):
    # Input
    user_query: str

    # Step 6
    research_scope: Dict[str, Any] = Field(default_factory=dict)
    plan: List[str] = Field(default_factory=list)

    # Step 7
    sources: List[Dict[str, Any]] = Field(default_factory=list)
    documents: List[Dict[str, Any]] = Field(default_factory=list)

    # Step 8 (NEW)
    embeddings_index: Optional[Any] = None
    embedded_docs: List[Dict[str, Any]] = Field(default_factory=list)

    # Later steps (placeholders – fine to keep)
    notes: List[Dict[str, Any]] = Field(default_factory=list)

    flags: List[Dict[str, Any]] = Field(default_factory=list)
    
    final_report: str = ""
    confidence_score: float = 0.0
