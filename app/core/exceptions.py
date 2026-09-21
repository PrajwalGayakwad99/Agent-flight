"""
AgentFlight — Domain Exception Hierarchy
All exceptions carry an HTTP status_code and a human-readable detail string
so FastAPI exception handlers can translate them into consistent JSON responses.
"""


class AgentFlightException(Exception):
    """Base class for all AgentFlight domain exceptions."""

    status_code: int = 500
    detail: str = "An unexpected error occurred."

    def __init__(self, detail: str | None = None, status_code: int | None = None) -> None:
        self.detail = detail or self.__class__.detail
        self.status_code = status_code or self.__class__.status_code
        super().__init__(self.detail)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(status_code={self.status_code}, detail={self.detail!r})"


# ── 404 Not Found ─────────────────────────────────────────────────────────────

class AgentNotFoundError(AgentFlightException):
    """Raised when an agent_id does not exist in the repository."""

    status_code: int = 404
    detail: str = "Agent not found."


# ── 422 Unprocessable Entity ──────────────────────────────────────────────────

class AdapterValidationError(AgentFlightException):
    """Raised when an adapter receives a malformed or unsupported payload."""

    status_code: int = 422
    detail: str = "Adapter validation failed."


# ── 400 Bad Request ───────────────────────────────────────────────────────────

class SpecParseException(AgentFlightException):
    """Raised when an uploaded spec (OpenAPI / JSON / YAML) cannot be parsed."""

    status_code: int = 400
    detail: str = "Failed to parse the provided specification."


# ── 403 Forbidden ─────────────────────────────────────────────────────────────

class SecurityGatewayError(AgentFlightException):
    """Raised by the security gateway when a request is rejected."""

    status_code: int = 403
    detail: str = "Access denied by the security gateway."


# ── 429 Too Many Requests ─────────────────────────────────────────────────────

class RateLimitExceededError(AgentFlightException):
    """Raised when a client exceeds the configured rate limit."""

    status_code: int = 429
    detail: str = "Rate limit exceeded. Please retry after a moment."
