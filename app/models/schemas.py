# Pydantic models for request and response data
from pydantic import BaseModel


class TextRequest(BaseModel):
    text: str


class AnalysisResponse(BaseModel):
    result: str
