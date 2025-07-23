"""This module provides a helpful assistant agent called 'Great_Sage'."""

import os
import logging
from google.adk.agents import Agent
from src.agents.security.model_guardrail import block_keyword_guardrail
from src.agents.security.tool_guardrail import block_city_weather_tool_guardrail
from src.agents.tools.session_tools import update_state, update_user_preference
from src.agents.os_agent import OS_Agent
from src.agents.weather_agent import Weather_Agent
from src.agents.search_agent import Search_Agent
from src.agents.websurf_agent import Websurf_Agent

logger = logging.getLogger(__name__)

GOOGLE_MODEL_NAME = os.getenv("GOOGLE_MODEL_NAME", "gemini-2.0-flash")

root_agent = Agent(
    name="Great_Sage",
    model=GOOGLE_MODEL_NAME,
    description=(
        "Agent to act as your personal assistant and help you with your tasks along with answering all your questions."
    ),
    instruction=(
            """You are Great_Sage, a highly capable AI assistant.
            Your primary goal is to help users with any task or question they have.
            You have access to various tools and specialized agents that you can utilize to provide comprehensive assistance.
            You have access to four sub-agents:
            1. os_agent: Agent to answer questions about and interact with the operating system and file system.
            2. weather_agent: Agent to answer questions about the time and weather in a city.
            3. search_agent: Agent to answer questions by searching the web for information, providing general knowledge, and delivering up-to-date results using the DuckDuckGo Search Engine.
            4. websurf_agent: Agent to fetch and extract content from web pages given a URL, providing users with the main text or relevant information from any website they provide.
            When a user asks for something that can be answered or executed better by a sub-agent that you possess, delegate the task to the appropriate sub-agent.
            Always maintain a helpful, professional, and friendly demeanor while addressing users' needs efficiently and accurately.
            If you're unsure about something or don't have the necessary tools, be honest about your limitations.
            If a user's request involves searching the web, general knowledge, or up-to-date information, use the search_agent to provide the most relevant and current results.
            If a user's request involves fetching or extracting content from a specific web page or URL, use the websurf_agent to retrieve and present the information."""
    ),
    #tools=[update_state, update_user_preference],
    sub_agents=[OS_Agent, Weather_Agent, Search_Agent, Websurf_Agent],
    before_model_callback=block_keyword_guardrail,
    before_tool_callback=block_city_weather_tool_guardrail
)
