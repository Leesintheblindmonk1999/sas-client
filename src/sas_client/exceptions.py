"""Exceptions for sas-client."""

from __future__ import annotations


class SASClientError(Exception):
    """Base exception for sas-client."""


class SASConnectionError(SASClientError):
    """Raised when the SAS API cannot be reached."""


class SASTimeoutError(SASConnectionError):
    """Raised when an API request times out."""


class SASAPIError(SASClientError):
    """Raised when the SAS API returns an error response."""

    def __init__(self, status_code: int, message: str, payload: dict | None = None):
        self.status_code = status_code
        self.payload = payload or {}
        super().__init__(f"SAS API error {status_code}: {message}")


class SASAuthenticationError(SASAPIError):
    """Raised when authentication fails."""
