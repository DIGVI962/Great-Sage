"""This module is the main entry point for the Great-Sage application."""

#import asyncio
import dotenv
import os
import uuid
import fastapi
from fastapi.middleware.cors import CORSMiddleware
import logging.config
from logging import DEBUG
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService, Session
from google.genai import types
import uvicorn
from agent import root_agent
from helpers.request_dto import StateRequest
from helpers.response_dto import StateResponse
from helpers.LlmEvents import LlmEvents
from logging_config import LOGGING_CONFIG


# --- Environment Setup ---
# Load environment variables if in debug mode
if DEBUG:
    dotenv.load_dotenv()
DEPLOYMENT_PORT = int(os.getenv("DEPLOYMENT_PORT", 10000))


# --- Logging Configuration ---
# Configure logging using the predefined logging configuration
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


# --- FastAPI Setup ---
# Initialize FastAPI application and configure CORS middleware
app = fastapi.FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Session Management ---
# SessionService stores conversation history & state.
session_service = InMemorySessionService()

APP_NAME = "Great_Sage"
USER_ID = "user_1"
SESSION_ID = str(uuid.uuid4())


# --- Runner Setup ---
# Orchestrates and maintains the agent runtime
runner = Runner(
    agent=root_agent,
    app_name=APP_NAME,
    session_service=session_service
)
logger.info(f"Runner created for agent '{runner.agent.name}'.")


# --- Session Management Functions ---
def create_session(user_id: str, session_id: str) -> None:
    """Function to create a new session to manage the conversation."""
    logger.info(f"Creating session with App='{APP_NAME}', User='{user_id}', Session='{session_id}'")

    session_service.create_session(
        app_name=APP_NAME,
        user_id=user_id,
        session_id=session_id
    )
    logger.info(f"Session created.")

def get_session(user_id: str, session_id: str) -> Session:
    """Function to get a session by user_id and session_id."""
    logger.info(f"Getting session with App='{APP_NAME}', User='{user_id}', Session='{session_id}'")

    session = session_service.get_session(app_name=APP_NAME, user_id=user_id, session_id=session_id)
    logger.info(f"Session retrieved.")

    return session


# --- Agent Interaction ---
async def call_agent_async(query: str, runner: Runner, user_id: str, session_id: str) -> tuple[str, list[LlmEvents]]:
    """Sends a query to the agent and returns the response."""
    logger.info(f"Calling agent with query: '{query}'")

    event_list = []
    content = types.Content(role='user', parts=[types.Part(text=query)])
    final_response_text = "Agent did not produce a response."

    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
        logger.info(f"  [Event] Author: {event.author}, Type: {type(event).__name__}, Final: {event.is_final_response()}, Content: {event.content}")
        event_element = LlmEvents(
            author=event.author,
            event_type=type(event).__name__,
            final=event.is_final_response(),
            content=event.content.parts[0].text if event.content and event.content.parts and len(event.content.parts) > 0 else None
        )
        event_list.append(event_element)

        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate:
                final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
                logger.error(final_response_text)
            break

    logger.info(f"Agent response: {final_response_text}")
    return (final_response_text or "Agent did not produce a response.", event_list)


# --- Conversation Loop ---
async def run_conversation() -> None:
    """Function to run the conversation."""
    logger.info("Starting Great-Sage...")

    user_id = input("Enter your user ID: ") or USER_ID
    session_id = input("Enter your session ID: ") or SESSION_ID
    
    if(get_session(user_id=user_id, session_id=session_id) is None):
        create_session(user_id=user_id, session_id=session_id)

    while True:
        try:
            user_input = input(">>> You: ")
            logger.info(f">>> You: {user_input}")

            if user_input.lower() in ['exit', 'quit']:
                logger.info("Exiting the conversation.")
                break
            else:
                response = await call_agent_async(query=user_input, runner=runner, user_id=user_id, session_id=session_id)
                print(f"<<< Agent Response: {response[0]}")
        except Exception as e:
            logger.error(f"An error occurred: {e}")


# --- API Endpoints ---
@app.post("/chat", response_model=StateResponse)
async def chat(request: StateRequest) -> StateResponse:
    """'POST' endpoint for chatting with the agent"""
    logger.info("Request on '/chat' endpoint.")

    user_query = request.query
    user_id = request.user_id or USER_ID
    session_id = request.session_id or SESSION_ID

    if(user_query is None or user_query.strip.len() == 0):
        return StateResponse(status=400, response="User query is empty or invalid.")

    if(get_session(user_id=user_id, session_id=session_id) is None):
        create_session(user_id=user_id, session_id=session_id)
    
    try:
        agent_response = await call_agent_async(query=user_query, runner=runner, user_id=user_id, session_id=session_id)
        return StateResponse(status=200, response=agent_response[0], events=agent_response[1])
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return StateResponse(status=500, response=e.__str__())


# --- Main Execution ---
# Run the FastAPI application
if __name__ == "__main__":
    try:
        uvicorn.run("main:app", host="0.0.0.0", port=DEPLOYMENT_PORT)
        #asyncio.run(run_conversation())
    except Exception as e:
        logger.error(f"An error occurred: {e}")
