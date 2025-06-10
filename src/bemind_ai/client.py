"""Main client for BeMind AI SDK."""

from typing import Optional, Dict, Any
import os
from .models import (
    SentimentResponse,
    EmotionResponse,
    TextGenerationResponse,
    ConversationAnalysisResponse,
)
from .exceptions import AuthenticationError, APIError
from .api import APIClient


class BeMindAI:
    """Main client for interacting with BeMind AI services."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: int = 30,
    ):
        """Initialize BeMind AI client.
        
        Args:
            api_key: API key for authentication. If not provided, will look for BEMIND_AI_API_KEY env var.
            base_url: Base URL for API. If not provided, will use default or BEMIND_AI_BASE_URL env var.
            timeout: Request timeout in seconds.
        """
        self.api_key = api_key or os.getenv("BEMIND_AI_API_KEY")
        if not self.api_key:
            raise AuthenticationError("API key is required. Set BEMIND_AI_API_KEY or pass api_key parameter.")
        
        self.base_url = base_url or os.getenv("BEMIND_AI_BASE_URL", "https://api.bemindlab.com/v1")
        self._client = APIClient(api_key=self.api_key, base_url=self.base_url, timeout=timeout)

    def analyze_sentiment(self, text: str, language: str = "auto") -> SentimentResponse:
        """Analyze sentiment of the given text.
        
        Args:
            text: Text to analyze.
            language: Language code or "auto" for automatic detection.
            
        Returns:
            SentimentResponse with sentiment analysis results.
        """
        response = self._client.post(
            "/sentiment/analyze",
            json={"text": text, "language": language}
        )
        return SentimentResponse(**response)

    def detect_emotions(self, text: str, language: str = "auto") -> EmotionResponse:
        """Detect emotions in the given text.
        
        Args:
            text: Text to analyze.
            language: Language code or "auto" for automatic detection.
            
        Returns:
            EmotionResponse with emotion detection results.
        """
        response = self._client.post(
            "/emotions/detect",
            json={"text": text, "language": language}
        )
        return EmotionResponse(**response)

    def generate_text(
        self,
        prompt: str,
        max_tokens: int = 100,
        temperature: float = 0.7,
        context: Optional[str] = None,
    ) -> TextGenerationResponse:
        """Generate text based on the prompt.
        
        Args:
            prompt: Text prompt for generation.
            max_tokens: Maximum number of tokens to generate.
            temperature: Sampling temperature (0-1).
            context: Optional context for generation.
            
        Returns:
            TextGenerationResponse with generated text.
        """
        response = self._client.post(
            "/text/generate",
            json={
                "prompt": prompt,
                "max_tokens": max_tokens,
                "temperature": temperature,
                "context": context,
            }
        )
        return TextGenerationResponse(**response)

    def analyze_conversation(
        self,
        messages: list[Dict[str, str]],
        include_suggestions: bool = True,
    ) -> ConversationAnalysisResponse:
        """Analyze a conversation for insights.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys.
            include_suggestions: Whether to include suggested responses.
            
        Returns:
            ConversationAnalysisResponse with analysis results.
        """
        response = self._client.post(
            "/conversation/analyze",
            json={
                "messages": messages,
                "include_suggestions": include_suggestions,
            }
        )
        return ConversationAnalysisResponse(**response)

    def get_mental_health_insights(self, text: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Get mental health insights from text.
        
        Args:
            text: Text to analyze.
            context: Optional context information.
            
        Returns:
            Dictionary with mental health insights.
        """
        response = self._client.post(
            "/mental-health/insights",
            json={"text": text, "context": context or {}}
        )
        return response