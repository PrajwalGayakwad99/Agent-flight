"""
AgentFlight — Response Normalization Utilities
Converts the raw output of any agent adapter (OpenAI-compatible, Ollama,
custom REST) into a single canonical structure so all downstream consumers
work against a stable contract.

Canonical response structure:
{
    "content":       str,    # The text/assistant message content
    "tool_calls":    list,   # Structured tool call objects (may be empty)
    "finish_reason": str,    # e.g. "stop", "tool_calls", "length", "error"
    "raw":           dict,   # Original unmodified response payload
    "latency_ms":    float,  # Round-trip latency in milliseconds
}
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)

# Protocols AgentFlight currently knows how to normalise
_KNOWN_PROTOCOLS = frozenset({"openai", "ollama", "custom_rest"})


def normalize_agent_response(
    raw_response: dict,
    protocol: str,
    latency_ms: float = 0.0,
) -> dict:
    """
    Normalise a raw adapter response into the AgentFlight canonical format.

    Args:
        raw_response: The unmodified dict returned by the agent adapter.
        protocol:     The adapter protocol that produced the response.
                      Supported values: "openai", "ollama", "custom_rest".
        latency_ms:   Optional round-trip latency measured by the caller.

    Returns:
        A dict with keys: content, tool_calls, finish_reason, raw, latency_ms.
    """
    protocol = protocol.lower().strip()

    if protocol not in _KNOWN_PROTOCOLS:
        logger.warning(
            "Unknown protocol %r — falling back to generic normalisation.", protocol
        )
        return _normalize_generic(raw_response, latency_ms)

    normaliser = _NORMALISERS[protocol]
    try:
        result = normaliser(raw_response)
    except Exception as exc:  # noqa: BLE001
        logger.error(
            "Normalisation failed for protocol %r: %s — returning raw payload.", protocol, exc
        )
        result = _empty_envelope()

    result["raw"] = raw_response
    result["latency_ms"] = float(latency_ms)
    return result


# ── Protocol-specific normalisers ─────────────────────────────────────────────

def _normalize_openai(raw: dict) -> dict:
    """Handles OpenAI-compatible chat-completion responses."""
    choices: list = raw.get("choices") or []
    if not choices:
        return _empty_envelope()

    message: dict = choices[0].get("message") or {}
    content: str = message.get("content") or ""
    tool_calls: list = message.get("tool_calls") or []
    finish_reason: str = choices[0].get("finish_reason") or "stop"

    # Normalise tool_calls to a consistent shape
    normalised_tool_calls = [
        {
            "id": tc.get("id", ""),
            "function": tc.get("function", {}).get("name", ""),
            "arguments": tc.get("function", {}).get("arguments", "{}"),
        }
        for tc in tool_calls
        if isinstance(tc, dict)
    ]

    return {
        "content": content,
        "tool_calls": normalised_tool_calls,
        "finish_reason": finish_reason,
    }


def _normalize_ollama(raw: dict) -> dict:
    """Handles Ollama /api/chat responses."""
    message: dict = raw.get("message") or {}
    content: str = message.get("content") or ""
    tool_calls: list = message.get("tool_calls") or []
    done_reason: str = raw.get("done_reason") or ("stop" if raw.get("done") else "unknown")

    normalised_tool_calls = [
        {
            "id": "",
            "function": tc.get("function", {}).get("name", ""),
            "arguments": str(tc.get("function", {}).get("arguments", {})),
        }
        for tc in tool_calls
        if isinstance(tc, dict)
    ]

    return {
        "content": content,
        "tool_calls": normalised_tool_calls,
        "finish_reason": done_reason,
    }


def _normalize_custom_rest(raw: dict) -> dict:
    """
    Handles arbitrary REST agent responses.
    Best-effort extraction: looks for common field names.
    """
    content: str = (
        raw.get("content")
        or raw.get("response")
        or raw.get("text")
        or raw.get("message")
        or raw.get("output")
        or ""
    )
    tool_calls: list = raw.get("tool_calls") or raw.get("tools") or []
    finish_reason: str = raw.get("finish_reason") or raw.get("stop_reason") or "stop"

    return {
        "content": str(content),
        "tool_calls": list(tool_calls),
        "finish_reason": str(finish_reason),
    }


def _normalize_generic(raw: dict, latency_ms: float) -> dict:
    """Fallback for unknown protocols."""
    result = _normalize_custom_rest(raw)
    result["raw"] = raw
    result["latency_ms"] = float(latency_ms)
    return result


def _empty_envelope() -> dict:
    return {
        "content": "",
        "tool_calls": [],
        "finish_reason": "error",
    }


_NORMALISERS: dict[str, object] = {
    "openai": _normalize_openai,
    "ollama": _normalize_ollama,
    "custom_rest": _normalize_custom_rest,
}
