# API endpoints
from fastapi import APIRouter
from ..services.text_processing import analyze_sentiment, extract_keywords, summarize_text
from ..models.schemas import TextRequest, AnalysisResponse

router = APIRouter()


@router.post("/analyze/sentiment", response_model=AnalysisResponse)
def sentiment_analysis(request: TextRequest):
    result = analyze_sentiment(request.text)
    return AnalysisResponse(result=result)


@router.post("/analyze/keywords", response_model=AnalysisResponse)
def keyword_extraction(request: TextRequest):
    result = extract_keywords(request.text)
    return AnalysisResponse(result=result)


@router.post("/analyze/summary", response_model=AnalysisResponse)
def text_summary(request: TextRequest):
    result = summarize_text(request.text)
    return AnalysisResponse(result=result)
