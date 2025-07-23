"""This module provides a map agent that can answer questions using DuckDuckGo Search Engine."""

import os
from google.adk.agents import LlmAgent
from src.agents.tools.search_tools import duckduckgo_search_tool

GOOGLE_MODEL_NAME = os.getenv("GOOGLE_MODEL_NAME", "gemini-2.0-flash")

Search_Agent = LlmAgent(
    name="search_agent",
    model=GOOGLE_MODEL_NAME,
    description=(
        "Agent to answer questions using DuckDuckGo Search Engine."
    ),
    instruction=(
            """You are an agent that can interact with the DuckDuckGo Search Engine.
            You can help users by searching the web for information, answering general knowledge questions, and providing up-to-date results from the internet.
            Use your access to DuckDuckGo to find relevant, accurate, and timely information in response to user queries."""
    ),
    tools=[duckduckgo_search_tool],
)
