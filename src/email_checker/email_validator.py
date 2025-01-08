import os
import httpx
from typing import Any
import logging

# Set up logging
logger = logging.getLogger(__name__)

class EmailValidatorAPI:
    """Handler for 2ip.me API interactions."""
    
    def __init__(self):
        self.api_base = "https://api.2ip.me/email.txt"
        
    async def make_request(self, email: str) -> str | None:
        """Make a request to the 2ip.me API with proper error handling."""
        url = f"{self.api_base}?email={email}"
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, timeout=30.0)
                response.raise_for_status()
                return response.text.strip()
            except Exception as e:
                logger.error(f"API request failed: {str(e)}")
                return None

    async def verify_email(self, email: str) -> str:
        """Verify an email address."""
        result = await self.make_request(email)
        if result is None:
            return "Error: Unable to verify email"
        return result 