"""
sas-client

Python client for SAS - Symbiotic Autoprotection System.
"""

from .client import SASClient
from .exceptions import SASAPIError, SASAuthenticationError, SASConnectionError, SASTimeoutError

__version__ = "0.1.0"

__all__ = [
    "SASClient",
    "SASAPIError",
    "SASAuthenticationError",
    "SASConnectionError",
    "SASTimeoutError",
]
