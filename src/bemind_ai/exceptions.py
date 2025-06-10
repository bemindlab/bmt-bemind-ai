"""Custom exceptions for BeMind AI SDK."""


class BeMindAIError(Exception):
    """Base exception for BeMind AI SDK."""
    
    pass


class AuthenticationError(BeMindAIError):
    """Raised when authentication fails."""
    
    pass


class APIError(BeMindAIError):
    """Raised when API request fails."""
    
    def __init__(self, message: str, status_code: int = None, response_data: dict = None):
        super().__init__(message)
        self.status_code = status_code
        self.response_data = response_data or {}