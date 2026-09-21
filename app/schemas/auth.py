"""
AgentFlight — Auth Schemas
Pydantic v2 models used by the authentication routes and JWT utilities.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    """Credentials submitted on the login endpoint."""

    username: str = Field(..., min_length=1, max_length=128, examples=["prajwal"])
    password: str = Field(..., min_length=1, max_length=256)


class TokenSchema(BaseModel):
    """JWT access token returned after successful login."""

    access_token: str = Field(..., description="Signed JWT bearer token.")
    token_type: str = Field(default="bearer", description="Always 'bearer'.")


class TokenData(BaseModel):
    """
    Claims extracted from a validated JWT.
    Injected into route handlers via the `get_current_user` dependency.
    """

    username: str = Field(..., description="Subject claim — the authenticated user's username.")
    role: str = Field(default="user", description="RBAC role (e.g. 'admin', 'user').")
