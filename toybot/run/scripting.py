import inspect

from ..languages.toybot import ToyBot
from ..renderer.console import ConsoleRenderer
from ..scenegraph.scenegraph import SceneGraph


def create_scripting_namespace(bot):
    namespace = {}
    for name, method in inspect.getmembers(bot, predicate=inspect.ismethod):
        if name.startswith("__"):
            continue
        namespace[name] = method
    return namespace


def run(source):
    graph = SceneGraph()
    renderer = ConsoleRenderer()

    bot = ToyBot(graph)
    namespace = create_scripting_namespace(bot)

    exec(source, namespace)

    renderer.render(graph)
