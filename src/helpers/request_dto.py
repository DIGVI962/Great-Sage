"""This module defines data transfer objects (DTOs) for request."""

from typing import Optional
from pydantic import BaseModel, Field

class StateRequest(BaseModel):
    """Request model for POST '/chat' endpoint.
    
    This model represents the request payload for the chat endpoint, containing the user's query, user ID, and session ID.
    """
    query: Optional[str] = Field(
        default = None,
        description = "The user's query or message for the chat endpoint."
    )

    user_id: Optional[str] = Field(
        default = None,
        description = "The unique identifier for the user making the request."
    )

    session_id: Optional[str] = Field(
        default = None,
        description = "The session identifier to maintain conversation context."
    )
