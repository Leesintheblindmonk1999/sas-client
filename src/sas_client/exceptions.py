"""Exceptions for sas-client."""

from __future__ import annotations

from typing import Any


class SASClientError(Exception):
    """Base exception for sas-client."""


class SASConnectionError(SASClientError):
    """Raised when the SAS API cannot be reached."""


class SASTimeoutError(SASConnectionError):
    """Raised when an API request times out."""


class SASAPIError(SASClientError):
    """Raised when the SAS API returns an error response."""

    def __init__(
        self,
        status_code: int,
        message: str,
        payload: dict[str, Any] | None = None,
    ) -> None:
        self.status_code = int(status_code)
        self.payload = payload or {}
        self.message = str(message)
        super().__init__(f"SAS API error {self.status_code}: {self.message}")


class SASAuthenticationError(SASAPIError):
    """Raised when authentication fails."""


class SASRateLimitError(SASAPIError):
    """Raised when the SAS API returns HTTP 429."""


class SASServerError(SASAPIError):
    """Raised when the SAS API returns a 5xx response."""
