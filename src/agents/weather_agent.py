"""This module provides a weather agent that can answer questions about the time and weather in a city."""

import os
from google.adk.agents import Agent
from src.agents.tools.weather_tools import get_weather_stateful, get_current_time

GOOGLE_MODEL_NAME = os.getenv("GOOGLE_MODEL_NAME", "gemini-2.0-flash")

Weather_Agent = Agent(
    name="weather_time_agent",
    model=GOOGLE_MODEL_NAME,
    description=(
        "Agent to answer questions about the time and weather (state-aware unit) in a city, saves report to state."
    ),
    instruction=(
        """You are a helpful agent who can answer user questions about the time and weather in a city.
        The tool will format the temperature based on user preference stored in state.
        """
    ),
    tools=[get_weather_stateful, get_current_time],
    output_key="last_weather_report" # <<< Auto-save agent's final weather response
)
