import json
from google.adk.agents import Agent

from google.adk.models.lite_llm import LiteLlm
import datetime
from zoneinfo import ZoneInfo
from . import prompt
from . import utils


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (f"Sorry, I don't have timezone information for {city}."),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = f"The current time in {city} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"
    return {"status": "success", "report": report}


def check_json(json_str: str) -> bool:
    """
    Check if the given string is a valid JSON.

    Args:
        json_str (str): The string to check.

    Returns:
        bool: True if the string is a valid JSON, False otherwise.
    """

    try:
        json.loads(json_str)
        return True
    except json.JSONDecodeError:
        return False


root_agent = Agent(
    name="gofood_recommendatio_agent",
    model=LiteLlm(model="openai/qwen-plus"),
    description=("Agent to calling and reading api "),
    instruction=prompt.FOOD_PROMPT,
    tools=[
        utils.search_restaurant_near_me,
        utils.get_restaurant_details,
        utils.get_merchant_promo,
        utils.search_restaurant_by_food_name,
        utils.get_restaurant_review,
        check_json,
    ],
)
