"""Optional lightweight models for users who prefer typed wrappers."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class SASResult:
    raw: dict[str, Any]

    @property
    def isi(self) -> float | None:
        value = self.raw.get("isi")
        return float(value) if value is not None else None

    @property
    def verdict(self) -> str | None:
        value = self.raw.get("verdict")
        return str(value) if value is not None else None

    @property
    def fired_modules(self) -> list[str]:
        evidence = self.raw.get("evidence") or {}
        modules = evidence.get("fired_modules") or self.raw.get("fired_modules") or []
        return [str(item) for item in modules]
