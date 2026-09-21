"""
AgentFlight — Agent Schemas
Pydantic v2 models covering the full lifecycle of an agent registration:
creation, storage, API responses, and profiling output.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Optional

from pydantic import BaseModel, Field, field_validator


class AuthenticationConfig(BaseModel):
    """
    Describes how AgentFlight authenticates outbound requests to an agent endpoint.
    Exactly one of `token` or `api_key` should be set for authenticated endpoints.
    """

    type: str = Field(
        default="bearer",
        description="Authentication scheme: 'bearer', 'api_key', or 'none'.",
    )
    token: Optional[str] = Field(
        default=None,
        description="Bearer token to include in the Authorization header.",
    )
    api_key: Optional[str] = Field(
        default=None,
        description="API key passed as a header or query parameter.",
    )

    @field_validator("type")
    @classmethod
    def validate_type(cls, v: str) -> str:
        allowed = {"bearer", "api_key", "none"}
        if v.lower() not in allowed:
            raise ValueError(f"authentication type must be one of {allowed}")
        return v.lower()


class AgentCreate(BaseModel):
    """
    Payload sent by the client to register a new agent.
    """

    name: str = Field(..., min_length=1, max_length=128, description="Human-readable agent name.")
    protocol: str = Field(
        ...,
        description="Adapter protocol: 'openai', 'ollama', or 'custom_rest'.",
    )
    endpoint_url: str = Field(..., description="Fully-qualified URL of the agent's inference endpoint.")
    model: Optional[str] = Field(
        default=None,
        description="Model identifier (e.g. 'gpt-4o', 'llama3:8b'). Optional at registration time.",
    )
    system_prompt: str = Field(
        default="",
        description="Optional system prompt prepended to every agent invocation.",
    )
    tools: list[dict[str, Any]] = Field(
        default_factory=list,
        description="Tool definitions the agent is allowed to call.",
    )
    authentication: AuthenticationConfig = Field(
        default_factory=AuthenticationConfig,
        description="Auth config for outbound requests to the agent endpoint.",
    )

    @field_validator("protocol")
    @classmethod
    def validate_protocol(cls, v: str) -> str:
        allowed = {"openai", "ollama", "custom_rest"}
        if v.lower() not in allowed:
            raise ValueError(f"protocol must be one of {allowed}")
        return v.lower()


class AgentResponse(BaseModel):
    """
    Full agent record returned by the API after creation or retrieval.
    """

    agent_id: str = Field(..., description="Unique agent identifier (e.g. 'agent_3f2a1c09b7e4').")
    name: str
    protocol: str
    endpoint_url: str
    model: Optional[str]
    system_prompt: str
    tools: list[dict[str, Any]]
    authentication: AuthenticationConfig
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class AgentProfile(BaseModel):
    """
    Condensed agent representation used when dispatching simulation payloads.
    Contains the subset of fields needed by the simulation workers.
    """

    agent_id: str = Field(..., description="Unique agent identifier.")
    name: str = Field(..., description="Human-readable agent name.")
    endpoint_url: str = Field(..., description="Inference endpoint URL.")
    protocol: str = Field(..., description="Adapter protocol.")
    system_prompt: str = Field(default="")
    tools: list[dict[str, Any]] = Field(default_factory=list)
    domain: str = Field(
        default="general",
        description="Inferred or declared domain (e.g. 'customer-support', 'coding').",
    )
    capabilities: list[str] = Field(
        default_factory=list,
        description="High-level capability tags derived by the agent profiler.",
    )
