"""
AgentFlight — Simulation Schemas
Pydantic v2 models for triggering and tracking simulation runs.
The simulation itself is executed by the LangGraph worker (out of scope for
this component); this backend publishes the trigger payload to Redis.
"""

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator

from app.schemas.agent import AgentProfile


class TestConfig(BaseModel):
    """
    Configuration knobs passed to the simulation worker controlling
    how many scenarios to generate and how adversarial to make them.
    """

    scenario_count: int = Field(
        default=5,
        ge=1,
        le=100,
        description="Number of test scenarios to generate and run.",
    )
    max_turns_per_scenario: int = Field(
        default=6,
        ge=1,
        le=50,
        description="Maximum conversation turns allowed per scenario.",
    )
    chaos_injection_rate: float = Field(
        default=0.3,
        ge=0.0,
        le=1.0,
        description="Fraction of turns where a chaos/fault event is injected (0.0–1.0).",
    )
    red_team_enabled: bool = Field(
        default=True,
        description="Whether the red-team adversarial agent should run against this simulation.",
    )

    @field_validator("chaos_injection_rate")
    @classmethod
    def round_rate(cls, v: float) -> float:
        return round(v, 4)


class SimulationTriggerPayload(BaseModel):
    """
    The complete payload published to Redis when a simulation is queued.
    LangGraph workers consume this message to begin scenario generation.
    """

    simulation_id: str = Field(
        ...,
        description="Unique simulation run identifier (e.g. 'sim_9d0e4b2a1c8f').",
    )
    agent_profile: AgentProfile = Field(
        ...,
        description="Condensed agent profile passed to the simulation worker.",
    )
    test_config: TestConfig = Field(
        default_factory=TestConfig,
        description="Configuration controlling scenario generation and adversarial settings.",
    )


class SimulationResponse(BaseModel):
    """
    Immediate HTTP response returned to the caller after a simulation is queued.
    Real-time progress is subsequently streamed over WebSocket.
    """

    simulation_id: str = Field(..., description="The queued simulation's unique ID.")
    status: str = Field(default="queued", description="Initial status: always 'queued'.")
    message: str = Field(
        default="Simulation queued successfully. Connect to WebSocket for live updates.",
        description="Human-readable status message.",
    )
