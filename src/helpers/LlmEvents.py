"""This module defines the LlmEvents model used for storing events related to LLM interactions."""

from typing import Optional
from pydantic import BaseModel, Field

class LlmEvents(BaseModel):
    """Model to store the event in LLM"""
    author: Optional[str] = Field(
        default = None,
        description="The author of the event (e.g., 'user', 'agent', 'tool')."
    )

    event_type: Optional[str] = Field(
        default = None,
        description="The type of the event (e.g., 'MessageEvent', 'ToolCodeEvent')."
    )

    final: Optional[bool] = Field(
        default = False,
        description="Indicates if this event is the final response from the agent."
    )

    content: Optional[str | None] = Field(
        default = None,
        description="The textual content of the event, if applicable."
    )
