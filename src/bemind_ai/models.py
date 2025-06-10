"""Data models for BeMind AI SDK."""

from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field


class SentimentResponse(BaseModel):
    """Response model for sentiment analysis."""
    
    sentiment: str = Field(..., description="Overall sentiment (positive, negative, neutral)")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score")
    scores: Dict[str, float] = Field(..., description="Detailed sentiment scores")
    language: str = Field(..., description="Detected or specified language")
    

class Emotion(BaseModel):
    """Individual emotion detection."""
    
    name: str = Field(..., description="Emotion name")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score")
    

class EmotionResponse(BaseModel):
    """Response model for emotion detection."""
    
    emotions: List[Emotion] = Field(..., description="Detected emotions")
    primary_emotion: str = Field(..., description="Primary detected emotion")
    language: str = Field(..., description="Detected or specified language")
    

class TextGenerationResponse(BaseModel):
    """Response model for text generation."""
    
    generated_text: str = Field(..., description="Generated text")
    tokens_used: int = Field(..., description="Number of tokens used")
    finish_reason: str = Field(..., description="Reason for completion")
    

class ConversationInsight(BaseModel):
    """Individual conversation insight."""
    
    type: str = Field(..., description="Type of insight")
    description: str = Field(..., description="Insight description")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score")
    

class SuggestedResponse(BaseModel):
    """Suggested conversation response."""
    
    text: str = Field(..., description="Suggested response text")
    intent: str = Field(..., description="Intent of the response")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score")
    

class ConversationAnalysisResponse(BaseModel):
    """Response model for conversation analysis."""
    
    overall_sentiment: str = Field(..., description="Overall conversation sentiment")
    insights: List[ConversationInsight] = Field(..., description="Conversation insights")
    suggested_responses: Optional[List[SuggestedResponse]] = Field(
        None, description="Suggested responses"
    )
    turn_sentiments: List[Dict[str, Any]] = Field(
        ..., description="Sentiment for each conversation turn"
    )