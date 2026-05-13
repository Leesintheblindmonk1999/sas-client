"""Authentication helpers and authenticated endpoint mixin for sas-client."""

from __future__ import annotations

import os
from typing import Any


def resolve_api_key(explicit_api_key: str | None = None) -> str | None:
    """
    Resolve an API key.

    Priority:
    1. Explicit api_key argument.
    2. SAS_API_KEY environment variable.
    3. SAS_KEY environment variable.
    """
    if explicit_api_key and explicit_api_key.strip():
        return explicit_api_key.strip()

    for env_name in ("SAS_API_KEY", "SAS_KEY"):
        value = os.getenv(env_name)
        if value and value.strip():
            return value.strip()

    return None


class SASAuthMixin:
    """Authenticated SAS API endpoints."""

    def whoami(self) -> dict[str, Any]:
        """Return account, plan, quota and key identity information."""
        return self._request("GET", "/v1/whoami", auth=True)
