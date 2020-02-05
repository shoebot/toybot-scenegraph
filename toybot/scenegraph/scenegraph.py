"""The scenegraph is a structure to represent graphics before they are rendered."""
from __future__ import annotations

from typing import Iterator, List

from .path import Path


class SceneGraph:
    """Minimal scenegraph, each node is a Path."""

    def __init__(self) -> None:  # noqa: D107
        self.nodes: List[Path] = []

    def add_node(self, node: Path) -> None:
        """Add a Path node the graph."""
        self.nodes.append(node)

    def __iter__(self) -> Iterator:
        """Iterate every node in the graph."""
        yield from self.nodes.__iter__()
