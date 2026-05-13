"""Public endpoint mixin for sas-client."""

from __future__ import annotations

from typing import Any


class SASPublicMixin:
    """Public SAS API endpoints that do not require an API key."""

    def health(self) -> dict[str, Any]:
        """Check the public /health endpoint."""
        return self._request("GET", "/health")

    def readyz(self) -> dict[str, Any]:
        """Check the public /readyz endpoint."""
        return self._request("GET", "/readyz")

    def public_stats(self) -> dict[str, Any]:
        """Return public aggregate API usage stats."""
        return self._request("GET", "/public/stats")

    def public_activity(self, *, limit: int = 100) -> dict[str, Any]:
        """Return public anonymized activity events."""
        safe_limit = max(1, min(int(limit), 100))
        return self._request("GET", f"/public/activity?limit={safe_limit}")

    def demo_audit(self, source: str, response: str) -> dict[str, Any]:
        """
        Run the public no-key SAS demo audit.

        This uses POST /public/demo/audit and does not require an API key.
        """
        return self._request(
            "POST",
            "/public/demo/audit",
            payload={"source": source, "response": response},
            auth=False,
        )

    def request_key(self, email: str, name: str | None = None) -> dict[str, Any]:
        """
        Request a personal Free SAS API key by email.

        This uses POST /public/request-key and does not require an API key.
        """
        payload: dict[str, Any] = {"email": email}
        if name:
            payload["name"] = name

        return self._request(
            "POST",
            "/public/request-key",
            payload=payload,
            auth=False,
        )

    def plans(self) -> dict[str, Any]:
        """Return static hosted plan information."""
        return {
            "status": "ok",
            "plans": [
                {
                    "id": "free",
                    "name": "SAS Free",
                    "price": "0",
                    "currency": "USD",
                    "limit": "50 requests/day",
                    "requires_api_key": True,
                    "request_key_endpoint": "/public/request-key",
                },
                {
                    "id": "pro",
                    "name": "SAS Pro",
                    "price": "99",
                    "currency": "USD",
                    "limit": "10,000 requests/month",
                    "requires_api_key": True,
                    "checkout": "Polar or Mercado Pago through hosted landing/API",
                },
            ],
        }
