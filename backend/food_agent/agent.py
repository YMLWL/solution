import json
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import datetime
import re
from typing import Dict, Any
from . import prompt
from . import utils


def extract_location_from_message(message: str) -> dict:
    """Extract location information from the message."""
    # ... existing code ...


def validate_location(location_data: dict) -> bool:
    """Validate if we have sufficient location data."""
    # ... existing code ...


def process_user_message(message: str) -> dict:
    """Process the user's message and extract relevant information."""
    # ... existing code ...


def check_json(json_str: str) -> bool:
    """Check if the given string is a valid JSON."""
    try:
        json.loads(json_str)
        return True
    except json.JSONDecodeError:
        return False


class FoodAgent(Agent):
    def __init__(self):
        # Define tools with proper Google ADK Tool format
        tools = [
            utils.search_restaurant_near_me,
            utils.get_restaurant_details,
            utils.get_merchant_promo,
            utils.search_restaurant_by_food_name,
            utils.get_restaurant_review,
            check_json,
        ]

        super().__init__(
            name="gofood_recommendation_agent",
            model=LiteLlm(model="openai/qwen-plus"),
            description="Expert food recommendation agent that helps users find the best food options based on location, preferences, and available promotions",
            instruction=prompt.FOOD_PROMPT,
            tools=tools,
        )

    def process_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process incoming messages with Google ADK format.

        Args:
            message: Dict containing message data in Google ADK format

        Returns:
            Dict containing the response in proper format
        """
        try:
            # Extract the actual message text from ADK format
            if isinstance(message, dict):
                user_message = message.get("message", "")
                if not user_message and "parts" in message:
                    parts = message.get("parts", [])
                    user_message = parts[0].get("text", "") if parts else ""
            else:
                user_message = str(message)

            # Process the message and extract location
            processed_data = process_user_message(user_message)

            if not processed_data["has_valid_location"]:
                return {
                    "role": "assistant",
                    "parts": [
                        {
                            "text": "Mohon maaf, saya membutuhkan informasi lokasi Anda untuk memberikan rekomendasi yang tepat. Bisa tolong share lokasi Anda?"
                        }
                    ],
                }

            # Create context for the model
            context = {
                "message": processed_data["clean_message"],
                "location": processed_data["location"],
                "timestamp": datetime.datetime.now().isoformat(),
                "language": "id",  # Default to Indonesian
            }

            # Call parent's process_message with context
            response = super().process_message(context)

            # Validate response format
            if isinstance(response, dict):
                if "error" in response:
                    return {
                        "role": "assistant",
                        "parts": [
                            {"text": f"Maaf, terjadi kesalahan: {response['error']}"}
                        ],
                    }

                # If it's already in the correct format, validate the JSON
                if check_json(json.dumps(response)):
                    return {
                        "role": "assistant",
                        "parts": [{"text": json.dumps(response, ensure_ascii=False)}],
                    }

            # If response is just text, wrap it in proper format
            return {"role": "assistant", "parts": [{"text": str(response)}]}

        except Exception as e:
            return {
                "role": "assistant",
                "parts": [{"text": f"Mohon maaf, terjadi kesalahan sistem: {str(e)}"}],
            }

    def handle_error(self, error: Exception) -> Dict[str, Any]:
        """
        Handle errors in a user-friendly way

        Args:
            error: The exception that occurred

        Returns:
            Dict containing error message in proper format
        """
        error_msg = "Mohon maaf, "
        if isinstance(error, requests.exceptions.RequestException):
            error_msg += "terjadi masalah koneksi ke layanan. Silakan coba lagi."
        elif isinstance(error, json.JSONDecodeError):
            error_msg += (
                "format data tidak valid. Tim kami sedang memperbaiki masalah ini."
            )
        else:
            error_msg += "terjadi kesalahan. Silakan coba lagi nanti."

        return {"role": "assistant", "parts": [{"text": error_msg}]}


# Initialize the agent
root_agent = FoodAgent()
