class ConsoleRenderer:
    """
    This renderer outputs its nodes to the console.
    """

    def render(self, graph):
        for node in graph:
            print(node)
