from typing import List
from pydantic import BaseModel

class ResearchState(BaseModel):
    topic: str
    research: str = ""
    report: str = ""
    source_urls: List[str] = []
    source_content: List[str] = []
    citations: List[str] = []
    citation_urls: List[str] = []


