import logging
from mcp.server.fastmcp import FastMCP
from .email_validator import EmailValidatorAPI

# Set up logging
logger = logging.getLogger(__name__)

# Initialize FastMCP server and API client
mcp = FastMCP("email-checker")
api = EmailValidatorAPI()

@mcp.tool()
async def verify_email(email: str) -> str:
    """
    Verify an email address using the 2ip.me API.

    Args:
        email (str): The email address to verify

    Returns:
        str: "true" or "false" indicating if the email is valid
    """
    return await api.verify_email(email)