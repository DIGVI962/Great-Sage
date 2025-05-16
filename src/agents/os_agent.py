"""This module provides an os agent that can answer questions about your personal system and the interact with it."""

import os
from google.adk.agents import Agent
from agents.tools.os_tool.os_tool import list_directory, read_file, path_exists, get_current_working_directory

GOOGLE_MODEL_NAME = os.getenv("GOOGLE_MODEL_NAME", "gemini-2.0-flash")

OS_Agent = Agent(
    name="os_agent",
    model=GOOGLE_MODEL_NAME,
    description=(
        "Agent to answer questions about and interact with the operating system and file system."
    ),
    instruction=(
        """You are an agent that can interact with the operating system and file system. 
        You have access to tools that allow you to list the contents of directories, read the content of files, check if a path exists, and get the current working directory. 
        Use these tools to answer user questions about the file system or perform requested actions like listing files or reading file content."""
    ),
    tools=[list_directory, read_file, path_exists, get_current_working_directory],
)
