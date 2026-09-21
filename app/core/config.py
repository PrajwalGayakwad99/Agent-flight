"""
AgentFlight — Core Configuration
Loads all runtime settings from environment variables / .env file.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # ── Application ──────────────────────────────────────────────────────────
    APP_NAME: str = "AgentFlight"
    APP_ENV: str = "development"
    DEBUG: bool = True

    # ── Server ───────────────────────────────────────────────────────────────
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    # ── Security ─────────────────────────────────────────────────────────────
    JWT_SECRET_KEY: str = "dev-secret-key"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRY_MINUTES: int = 60

    # ── Redis ────────────────────────────────────────────────────────────────
    REDIS_URL: str = "redis://localhost:6379/0"

    # ── Gateway policies ─────────────────────────────────────────────────────
    REQUEST_TIMEOUT_SECONDS: int = 30
    RATE_LIMIT_PER_MINUTE: int = 60


# Global singleton — import this everywhere
settings = Settings()
