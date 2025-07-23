"""This module provides tools for interacting with the DuckDuckGo Search Engine."""

from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

command = "docker"
args = ["run", "-i", "--rm", "mcp/duckduckgo"]

duckduckgo_search_tool = MCPToolset(
    connection_params=StdioServerParameters(
        command=command,
        args=args,
    )
)
