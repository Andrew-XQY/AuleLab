"""API registration stubs for future orchestrators.

This module will eventually expose helpers that register high-level
interfaces (CLI commands, HTTP endpoints, notebooks, etc.) with whatever
runtime the toolkit is plugged into. For now it just documents the intent
so contributors know where to add their hooks.
"""
from __future__ import annotations

from typing import Any, Protocol


class Registry(Protocol):
    """Shallow protocol representing whatever registry we plug into."""

    def add(self, name: str, handler: Any, /, **metadata: Any) -> None:  # pragma: no cover - placeholder
        ...


def register_api(registry: Registry) -> None:
    """Register AuleLab API surfaces with *registry*.

    In the short term this function will probably wire CLI commands and
    service endpoints. For now it simply documents what needs to happen so
    future contributors have a single touch point.
    """

    # TODO: wire up real handlers once the orchestration surface is defined.
    registry.add("aulelabs.placeholder", lambda **_: None, purpose="bootstrap stub")
