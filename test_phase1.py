# test_phase1.py
import sys
sys.stdout.reconfigure(encoding="utf-8")  # Windows cp1252 safe-guard for emoji output
import datetime
from app.core.config import settings
from app.core.exceptions import AgentNotFoundError, AdapterValidationError
from app.utils.ids import generate_agent_id, generate_simulation_id
from app.utils.normalization import normalize_agent_response
from app.schemas.agent import AgentCreate, AgentProfile
from app.schemas.simulation import SimulationTriggerPayload, TestConfig
from app.schemas.events import WebSocketEventEnvelope

def test_phase_1():
    print("--- 1. Testing Config ---")
    print(f"App Name: {settings.APP_NAME}")
    print(f"Environment: {settings.APP_ENV}")
    print(f"Timeout: {settings.REQUEST_TIMEOUT_SECONDS}s")

    print("\n--- 2. Testing Utilities & ID Generation ---")
    agent_id = generate_agent_id()
    sim_id = generate_simulation_id()
    print(f"Generated Agent ID: {agent_id}")
    print(f"Generated Sim ID: {sim_id}")

    raw_response = {
        "choices": [{"message": {"content": "Hello World"}}],
        "usage": {"total_tokens": 10}
    }
    normalized = normalize_agent_response(raw_response, protocol="openai")
    print(f"Normalized Response Content: {normalized['content']}")

    print("\n--- 3. Testing Pydantic Schemas ---")
    agent_in = AgentCreate(
        name="Test Support Agent",
        protocol="custom_rest",
        endpoint_url="https://api.example.com/chat"
    )
    print(f"Validated Agent Input: {agent_in.name}")

    profile = AgentProfile(
        agent_id=agent_id,
        name=agent_in.name,
        protocol=agent_in.protocol,
        endpoint_url=agent_in.endpoint_url,
        domain="customer_service",
        capabilities=["chat", "lookup"]
    )
    
    payload = SimulationTriggerPayload(
        simulation_id=sim_id,
        agent_profile=profile,
        test_config=TestConfig(scenario_count=3)
    )
    print(f"Simulation Payload JSON Validated: {payload.simulation_id}")

    ws_event = WebSocketEventEnvelope(
        event="agent_message",
        simulation_id=sim_id,
        timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        data={"message": "Hello"}
    )
    print(f"WebSocket Envelope Created: {ws_event.event}")

    print("\n--- 4. Testing Exceptions ---")
    try:
        raise AgentNotFoundError("agent_123")
    except AgentNotFoundError as e:
        print(f"Caught Exception: {e.detail} (Status: {e.status_code})")

    print("\n✅ PHASE 1 ALL CHECKS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    test_phase_1()