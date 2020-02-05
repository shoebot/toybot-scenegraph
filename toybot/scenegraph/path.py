"""Paths.

The Toybot implementation of Paths is minimal, to
make it implementation across different backends
easier.
"""
from typing import List, Optional, Tuple

Point = Tuple[float, float]


class Path(object):
    """Small Path implementation."""

    type = "path"

    coords: List[Point]

    def __init__(self, coords: Optional[Point] = None) -> None:
        """Intialise Path."""
        self.coords: coords if coords else []

    def add_point(self, x: float, y: float) -> None:
        """Add point to end of Path."""
        self.coords.append((x, y))

    def __repr__(self) -> str:  # noqa: D105
        return f"<Path: {self.coords}>"
