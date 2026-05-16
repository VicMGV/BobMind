from pydantic import BaseModel
from typing import List, Dict, Any


class AnalysisResponse(BaseModel):
    """Response model for document analysis"""
    analysis: str
    profile: str
    question: str


class SummaryResponse(BaseModel):
    """Response model for document summarization"""
    summary: str
    profile: str


class HypothesisResponse(BaseModel):
    """Response model for hypothesis generation"""
    hypothesis: str
    profile: str
    documents_count: int
