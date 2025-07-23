"""This module provides a map agent that can fetch content from a URL provided by the user."""

import os
from google.adk.agents import LlmAgent
from src.agents.tools.websurf_tools import websurf_tool

GOOGLE_MODEL_NAME = os.getenv("GOOGLE_MODEL_NAME", "gemini-2.0-flash")

Websurf_Agent = LlmAgent(
    name="websurf_agent",
    model=GOOGLE_MODEL_NAME,
    description=(
        "Agent to fetch content from a URL provided by the user."
    ),
    instruction=(
        """You are an agent that can fetch and extract content from web pages given a URL.
        Assist users by retrieving the main text or relevant information from any website they provide.
        Use your web content fetching capabilities to deliver accurate and useful results in response to user queries."""
    ),
    tools=[websurf_tool],
)
