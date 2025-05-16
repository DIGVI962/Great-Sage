"""This module provides tools for getting weather and time information."""

import datetime
from zoneinfo import ZoneInfo
import logging

logger = logging.getLogger(__name__)

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """

    logger.info(f"Getting weather for {city}")

    if city.lower() == "new york":
        
        logger.info(f"Weather information for '{city}' is available.")

        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (77 degrees Fahrenheit)."
            ),
        }
    else:
        logger.error(f"Weather information for '{city}' is not available.")

        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }

def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    logger.info(f"Getting current time for {city}")

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:

        logger.error(f"Timezone information for '{city}' is not available.")

        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )

    logger.info(f"Current time for {city}: {report}")

    return {"status": "success", "report": report}
