class SceneGraph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def __iter__(self):
        """
        Iterator that yields every node in the graph
        """
        for node in self.nodes:
            yield node
