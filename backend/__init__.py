"""UEFN Physics — Store desktop plugin (bundles the physics skill pack)."""

from __future__ import annotations


def register(api) -> None:
    """Skill-only pack: no MCP tools; register marks the plugin loaded."""
    api.log("physics skill plugin registered")
