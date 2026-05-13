"""sas-client Python client for SAS - Symbiotic Autoprotection System."""

from .auth import resolve_api_key
from .client import DEFAULT_BASE_URL, SASClient
from .exceptions import (
    SASAPIError,
    SASAuthenticationError,
    SASClientError,
    SASConnectionError,
    SASRateLimitError,
    SASServerError,
    SASTimeoutError,
)

__version__ = "0.2.0"

__all__ = [
    "DEFAULT_BASE_URL",
    "SASClient",
    "SASClientError",
    "SASAPIError",
    "SASAuthenticationError",
    "SASConnectionError",
    "SASRateLimitError",
    "SASServerError",
    "SASTimeoutError",
    "resolve_api_key",
]
