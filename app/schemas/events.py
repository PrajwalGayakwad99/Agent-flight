"""
AgentFlight — Event Schemas
Pydantic v2 models for WebSocket messages streamed to the frontend
during a live simulation run.

Every message sent over the WebSocket connection is wrapped in a
`WebSocketEventEnvelope` to provide consistent routing information.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Optional

from pydantic import BaseModel, Field


class WebSocketEventEnvelope(BaseModel):
    """
    Standard wrapper for all real-time WebSocket events.

    Consumers can switch on the `event` field to route messages:
        "simulation.started"    — simulation worker has begun
        "scenario.started"      — a new scenario is being executed
        "turn.completed"        — one conversation turn finished
        "chaos.injected"        — a fault event was injected
        "scenario.completed"    — scenario finished with results
        "simulation.completed"  — all scenarios done, final report ready
        "simulation.error"      — an unrecoverable error occurred
    """

    event: str = Field(
        ...,
        description="Dot-separated event type (e.g. 'turn.completed').",
    )
    simulation_id: str = Field(
        ...,
        description="Identifies which simulation run this event belongs to.",
    )
    scenario_id: Optional[str] = Field(
        default=None,
        description="Identifies the scenario within the run (None for run-level events).",
    )
    turn: Optional[int] = Field(
        default=None,
        ge=0,
        description="Conversation turn index within the scenario (None for scenario-level events).",
    )
    timestamp: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat(),
        description="ISO-8601 UTC timestamp when the event was emitted.",
    )
    data: dict[str, Any] = Field(
        default_factory=dict,
        description="Event-specific payload; schema varies by event type.",
    )
