import logging
import asyncio
from .tools import mcp

# Set up logging
logger = logging.getLogger(__name__)

def main():
    """Entry point for the email validation service."""
    logger.info("Starting Email Validation server")
    try:
        mcp.run(transport='stdio')
        logger.info("Server initialized successfully")
    except Exception as e:
        logger.error(f"Server error occurred: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    main()