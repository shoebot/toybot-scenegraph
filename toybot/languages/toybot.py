"""Code specific to the ToyBot language."""
from typing import Optional, Tuple

from toybot.scenegraph import Path, SceneGraph

Color = Tuple[float, ...]


class ToyBot:
    """Minimal Bot language."""

    def __init__(self, graph: SceneGraph) -> None:
        """Attach SceneGraph instance for the bot to output graphics commands to."""
        self.graph: SceneGraph = graph

    def rect(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        fill: Optional[Color] = None,
        stroke: Optional[Color] = None,
    ) -> None:
        """Create a rectangular Path and add it to the SceneGraph."""
        p = Path(
            coords=[(x, y), (x, y + height), (x + width, y + height), (x + width, y)]
        )
        self.graph.add_node(p)
        return p
