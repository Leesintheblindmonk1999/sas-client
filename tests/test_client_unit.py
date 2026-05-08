import json
import urllib.error
from unittest.mock import patch

import pytest

from sas_client import SASClient
from sas_client.exceptions import SASAPIError, SASAuthenticationError


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload
    def __enter__(self):
        return self
    def __exit__(self, *args):
        return None
    def read(self):
        return json.dumps(self.payload).encode("utf-8")


def test_health_calls_health_endpoint():
    client = SASClient(base_url="https://example.test")
    with patch("urllib.request.urlopen", return_value=FakeResponse({"status": "ok"})) as mocked:
        assert client.health() == {"status": "ok"}
        request = mocked.call_args.args[0]
        assert request.full_url == "https://example.test/health"


def test_diff_sends_api_key_header():
    client = SASClient(base_url="https://example.test", api_key="sas_key")
    with patch("urllib.request.urlopen", return_value=FakeResponse({"isi": 0.42})) as mocked:
        result = client.diff(text_a="A", text_b="B")
        assert result["isi"] == 0.42
        request = mocked.call_args.args[0]
        assert request.get_header("X-api-key") == "sas_key"


def test_403_raises_authentication_error():
    client = SASClient(base_url="https://example.test", api_key="bad")
    error = urllib.error.HTTPError(url="https://example.test/v1/diff", code=403, msg="Forbidden", hdrs=None, fp=None)
    error.read = lambda: b'{"detail":"Forbidden"}'
    with patch("urllib.request.urlopen", side_effect=error):
        with pytest.raises(SASAuthenticationError):
            client.diff(text_a="A", text_b="B")


def test_500_raises_api_error():
    client = SASClient(base_url="https://example.test")
    error = urllib.error.HTTPError(url="https://example.test/health", code=500, msg="Server error", hdrs=None, fp=None)
    error.read = lambda: b'{"detail":"Internal server error"}'
    with patch("urllib.request.urlopen", side_effect=error):
        with pytest.raises(SASAPIError):
            client.health()
