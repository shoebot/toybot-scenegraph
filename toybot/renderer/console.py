import jsons


class ConsoleRenderer:
    """This renderer outputs its nodes to the console.
    """

    def __init__(self, outputformat=jsons.dumps):
        if not outputformat:
            outputformat = lambda data: data
        self.outputformat = outputformat

    def render(self, graph):
        print(self.outputformat([node for node in graph]))
