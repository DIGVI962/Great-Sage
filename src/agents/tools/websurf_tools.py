"""This module provides tools to fetch content from a URL provided by the user."""

from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
import logging

logger = logging.getLogger(__name__)

PATH_TO_YOUR_MCP_SERVER_SCRIPT = r"C:\Users\IAmTheWizard\Desktop\New folder (2)\Projects\Python\AgenticPractice\local-mcp-server\main.py" # <<< REPLACE

if PATH_TO_YOUR_MCP_SERVER_SCRIPT == "/path/to/your/my_adk_mcp_server.py":
    logger.error("PATH_TO_YOUR_MCP_SERVER_SCRIPT is not set. Please update it in agent.py.")

websurf_tool = MCPToolset(
    connection_params=StdioServerParameters(
        command='python3', # Command to run your MCP server script
        args=[PATH_TO_YOUR_MCP_SERVER_SCRIPT], # Argument is the path to the script
    )
    # tool_filter=['load_web_page'] # Optional: ensure only specific tools are loaded
)
