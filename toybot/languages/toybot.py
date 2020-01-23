from ..scenegraph.path import Path


class ToyBot:
    def __init__(self, graph):
        self.graph = graph

    def rect(self, x, y, width, height, fill=None, stroke=None):
        p = Path(
            coords=[(x, y), (x, y + height), (x + width, y + height), (x + width, y)]
        )
        self.graph.add_node(p)
        return p
