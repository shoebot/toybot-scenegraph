"""Script execution and support."""
import inspect
from typing import Any, Dict

from toybot.languages import ToyBot
from toybot.renderer import ConsoleRenderer
from toybot.scenegraph import SceneGraph


def create_scripting_namespace(bot: ToyBot) -> Dict[str, Any]:
    """
    Populate namespace in which to run the bot.

    :param bot: All attributes of bot will be added to a dictionary.
    :return: Dictionary containing bot namespace.
    """
    namespace = {}
    for name, method in inspect.getmembers(bot, predicate=inspect.ismethod):
        if name.startswith("__"):
            continue
        namespace[name] = method
    return namespace


def run(source: str) -> None:
    """
    Run bot source.

    Takes source, sets up Bot infrastructure and runs it.
    :param source: Bot source to execute.
    """
    graph = SceneGraph()
    renderer = ConsoleRenderer()

    bot = ToyBot(graph)
    namespace = create_scripting_namespace(bot)

    exec(source, namespace)  # noqa

    renderer.render(graph)
