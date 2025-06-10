"""Tests for BeMind AI client."""

import pytest
from unittest.mock import Mock, patch
from bemind_ai import BeMindAI, AuthenticationError
from bemind_ai.models import SentimentResponse


class TestBeMindAI:
    """Test cases for BeMindAI client."""
    
    def test_init_without_api_key(self):
        """Test initialization without API key raises error."""
        with patch.dict('os.environ', {}, clear=True):
            with pytest.raises(AuthenticationError):
                BeMindAI()
    
    def test_init_with_api_key(self):
        """Test initialization with API key."""
        client = BeMindAI(api_key="test-key")
        assert client.api_key == "test-key"
    
    def test_init_with_env_api_key(self):
        """Test initialization with environment variable."""
        with patch.dict('os.environ', {'BEMIND_AI_API_KEY': 'env-test-key'}):
            client = BeMindAI()
            assert client.api_key == "env-test-key"
    
    @patch('bemind_ai.client.APIClient')
    def test_analyze_sentiment(self, mock_api_client):
        """Test sentiment analysis."""
        # Setup mock
        mock_client = Mock()
        mock_client.post.return_value = {
            "sentiment": "positive",
            "confidence": 0.95,
            "scores": {"positive": 0.95, "negative": 0.03, "neutral": 0.02},
            "language": "en"
        }
        mock_api_client.return_value = mock_client
        
        # Test
        client = BeMindAI(api_key="test-key")
        result = client.analyze_sentiment("I love this!")
        
        # Assertions
        assert isinstance(result, SentimentResponse)
        assert result.sentiment == "positive"
        assert result.confidence == 0.95
        mock_client.post.assert_called_once_with(
            "/sentiment/analyze",
            json={"text": "I love this!", "language": "auto"}
        )