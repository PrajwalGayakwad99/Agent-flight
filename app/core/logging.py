"""
AgentFlight — Logging Configuration
Call `setup_logging()` once at application startup (inside `main.py`).
All modules should obtain loggers via `logging.getLogger(__name__)`.
"""

import logging
import sys


def setup_logging(level: int = logging.INFO) -> None:
    """
    Configure the root logger with a consistent format.

    Args:
        level: Logging level (default INFO). Pass `logging.DEBUG` when
               `settings.DEBUG` is True for verbose output.
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
        force=True,  # Override any existing handler configuration
    )

    # Silence overly chatty third-party loggers at WARNING level
    for noisy in ("httpx", "httpcore", "uvicorn.access"):
        logging.getLogger(noisy).setLevel(logging.WARNING)

    logging.getLogger(__name__).info("Logging initialised at level %s.", logging.getLevelName(level))
