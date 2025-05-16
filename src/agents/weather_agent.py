"""This module provides a weather agent that can answer questions about the time and weather in a city."""

import os
from google.adk.agents import Agent
from agents.tools.weather_tool.weather_tool import get_weather, get_current_time

GOOGLE_MODEL_NAME = os.getenv("GOOGLE_MODEL_NAME", "gemini-2.0-flash")

Weather_Agent = Agent(
    name="weather_time_agent",
    model=GOOGLE_MODEL_NAME,
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),
    tools=[get_weather, get_current_time],
)
