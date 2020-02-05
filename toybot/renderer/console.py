"""Console render target.

Provides a Console render target for debugging.

Data is passed to the console, with an option for JSON encoding.
"""
from typing import Callable, Optional

import jsons

from toybot.scenegraph import SceneGraph


class ConsoleRenderer:
    """This renderer outputs its nodes to the console."""

    def __init__(self, outputformat: Optional[Callable] = jsons.dumps) -> None:
        """:param outputformat: Pass in a callable to transorm data before output."""  # noqa: D104
        if not outputformat:
            outputformat = lambda data: data  # noqa
        self.outputformat = outputformat

    def render(self, graph: SceneGraph) -> None:
        """
        Output all nodes to stdout.

        The output is transformed by the outputformat callable.
        """
        print(self.outputformat([node for node in graph]))
