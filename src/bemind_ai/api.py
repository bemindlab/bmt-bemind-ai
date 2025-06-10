"""API client for making HTTP requests."""

from typing import Optional, Dict, Any
import httpx
from .exceptions import APIError, AuthenticationError


class APIClient:
    """HTTP client for API requests."""
    
    def __init__(self, api_key: str, base_url: str, timeout: int = 30):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "BeMind-AI-SDK/0.1.0",
        }
    
    def _handle_response(self, response: httpx.Response) -> Dict[str, Any]:
        """Handle API response and raise appropriate exceptions."""
        if response.status_code == 401:
            raise AuthenticationError("Invalid API key or authentication failed")
        
        if response.status_code >= 400:
            try:
                error_data = response.json()
            except Exception:
                error_data = {"error": response.text}
            
            raise APIError(
                message=error_data.get("error", f"API request failed with status {response.status_code}"),
                status_code=response.status_code,
                response_data=error_data
            )
        
        return response.json()
    
    def post(self, endpoint: str, json: Dict[str, Any]) -> Dict[str, Any]:
        """Make POST request to API."""
        url = f"{self.base_url}{endpoint}"
        
        with httpx.Client(timeout=self.timeout) as client:
            response = client.post(url, json=json, headers=self.headers)
            return self._handle_response(response)
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make GET request to API."""
        url = f"{self.base_url}{endpoint}"
        
        with httpx.Client(timeout=self.timeout) as client:
            response = client.get(url, params=params, headers=self.headers)
            return self._handle_response(response)