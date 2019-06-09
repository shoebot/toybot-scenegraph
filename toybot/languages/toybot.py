class ToyBot:
    def __init__(self, graph):
        self.graph = graph

    def rect(self, x, y, width, height, fill=None, stroke=None):
        coords = [(x, y), (x, y + height), (x + width, y + height), (x + width, y)]
        node = {"type": "path", "coords": coords}

        self.graph.add_node(node)
