"""SAS API client.

No third-party runtime dependencies.
Uses Python standard library urllib.
"""

from __future__ import annotations

import json
import socket
import urllib.error
import urllib.request
from typing import Any

from .auth import SASAuthMixin, resolve_api_key
from .exceptions import (
    SASAPIError,
    SASAuthenticationError,
    SASConnectionError,
    SASRateLimitError,
    SASServerError,
    SASTimeoutError,
)
from .public import SASPublicMixin

DEFAULT_BASE_URL = "https://sas-api.onrender.com"


class SASClient(SASPublicMixin, SASAuthMixin):
    """Python client for SAS - Symbiotic Autoprotection System."""

    def __init__(
        self,
        *,
        base_url: str = DEFAULT_BASE_URL,
        api_key: str | None = None,
        timeout: float = 30.0,
        user_agent: str = "sas-client-python/0.2.0",
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = resolve_api_key(api_key)
        self.timeout = float(timeout)
        self.user_agent = user_agent

    def _headers(self, *, auth: bool = False) -> dict[str, str]:
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": self.user_agent,
        }

        if auth:
            if not self.api_key:
                raise SASAuthenticationError(
                    401,
                    "Missing API key. Set SAS_API_KEY, SAS_KEY, or pass api_key=...",
                    {},
                )
            headers["X-API-Key"] = self.api_key

        return headers

    def _request(
        self,
        method: str,
        path: str,
        *,
        payload: dict[str, Any] | None = None,
        auth: bool = False,
    ) -> dict[str, Any]:
        url = f"{self.base_url}{path}"
        body = json.dumps(payload).encode("utf-8") if payload is not None else None

        request = urllib.request.Request(
            url,
            data=body,
            headers=self._headers(auth=auth),
            method=method.upper(),
        )

        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                raw = response.read().decode("utf-8")
                return json.loads(raw) if raw else {}

        except urllib.error.HTTPError as exc:
            raw = exc.read().decode("utf-8", errors="replace")
            payload_data: dict[str, Any] = {}

            try:
                payload_data = json.loads(raw) if raw else {}
                message = (
                    payload_data.get("detail")
                    or payload_data.get("message")
                    or payload_data.get("error")
                    or raw
                    or exc.reason
                )
            except Exception:
                message = raw or str(exc.reason)

            if exc.code in {401, 403}:
                raise SASAuthenticationError(exc.code, str(message), payload_data) from exc
            if exc.code == 429:
                raise SASRateLimitError(exc.code, str(message), payload_data) from exc
            if exc.code >= 500:
                raise SASServerError(exc.code, str(message), payload_data) from exc

            raise SASAPIError(exc.code, str(message), payload_data) from exc

        except socket.timeout as exc:
            raise SASTimeoutError(
                f"SAS API request timed out after {self.timeout}s"
            ) from exc

        except urllib.error.URLError as exc:
            reason = getattr(exc, "reason", exc)
            raise SASConnectionError(f"Could not connect to SAS API: {reason}") from exc

        except json.JSONDecodeError as exc:
            raise SASConnectionError("SAS API returned invalid JSON") from exc

    def audit(self, text: str, *, experimental: bool = True) -> dict[str, Any]:
        """Audit a single text through POST /v1/audit."""
        return self._request(
            "POST",
            "/v1/audit",
            payload={"text": text, "experimental": experimental},
            auth=True,
        )

    def diff(
        self,
        *,
        text_a: str,
        text_b: str,
        experimental: bool = True,
    ) -> dict[str, Any]:
        """Compare source and response text through POST /v1/diff."""
        return self._request(
            "POST",
            "/v1/diff",
            payload={
                "text_a": text_a,
                "text_b": text_b,
                "experimental": experimental,
            },
            auth=True,
        )

    def chat(self, message: str, *, experimental: bool = True) -> dict[str, Any]:
        """Send one message through POST /v1/chat."""
        return self._request(
            "POST",
            "/v1/chat",
            payload={"message": message, "experimental": experimental},
            auth=True,
        )
