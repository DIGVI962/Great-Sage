"""
This module contains security guardrails for the agent.

It provides functions to inspect incoming requests and potentially block them
based on predefined criteria, such as the presence of blocked keywords.
"""

import logging
from typing import Optional
from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse
from google.genai import types
from src.agents.security.blocked_keywords import BLOCKED_KEYWORDS

logger = logging.getLogger(__name__)

def block_keyword_guardrail(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    """
    Inspects the latest user message for pre-defined BLOCKED_KEYWORDS. If found, blocks the LLM call
    and returns a predefined LlmResponse. Otherwise, returns None to proceed.
    """

    agent_name = callback_context.agent_name
    logger.info(f"--- Callback: block_keyword_guardrail running for agent: {agent_name} ---")

    last_user_message_text = ""
    if llm_request.contents:
        for content in reversed(llm_request.contents):
            if content.role == 'user' and content.parts:
                if content.parts[0].text:
                    last_user_message_text = content.parts[0].text
                    break
        
    logger.info(f"--- Callback: Inspecting last user message: '{last_user_message_text[:100]}...' ---")

    # --- Guardrail Logic ---
    for keyword_to_block in BLOCKED_KEYWORDS:
        if keyword_to_block in last_user_message_text.upper():
            logger.info(f"--- Callback: Found '{keyword_to_block}'. Blocking LLM call! ---")
            # Optionally, set a flag in state to record the block event
            callback_context.state["guardrail_block_keyword_triggered"] = True
            logger.info(f"--- Callback: Set state 'guardrail_block_keyword_triggered': True ---")

            # Construct and return an LlmResponse to stop the flow and send this back instead
            return LlmResponse(
                content=types.Content(
                    role='model',
                    parts=[types.Part(text=f"I cannot process this request because it contains the blocked keyword '{keyword_to_block}'.")],
                )
            )
        
    logger.info(f"--- Callback: Keyword not found. Allowing LLM call for {agent_name}. ---")
    return None
