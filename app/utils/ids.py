"""
AgentFlight — ID Generation Utilities
All entity IDs are short, human-readable strings built from a domain prefix
and the first 12 hex characters of a UUID4.

Examples:
    agent_3f2a1c09b7e4
    sim_9d0e4b2a1c8f
    spec_7c3b5a2d0e1f
    step_1a4f8c3e7b20
"""

import uuid


def _short_uuid() -> str:
    """Return the first 12 hex characters of a random UUID4."""
    return uuid.uuid4().hex[:12]


def generate_agent_id() -> str:
    """Generate a unique identifier for a registered agent."""
    return f"agent_{_short_uuid()}"


def generate_simulation_id() -> str:
    """Generate a unique identifier for a simulation run."""
    return f"sim_{_short_uuid()}"


def generate_spec_id() -> str:
    """Generate a unique identifier for an uploaded API spec."""
    return f"spec_{_short_uuid()}"


def generate_step_id() -> str:
    """Generate a unique identifier for a single simulation step / turn."""
    return f"step_{_short_uuid()}"
