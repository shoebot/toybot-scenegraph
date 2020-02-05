# noqa: D100 TODO write docstring here
from toybot.languages.toybot import ToyBot
from toybot.run.scripting import create_scripting_namespace
from toybot.scenegraph.scenegraph import SceneGraph


def test_create_scripting_namespace() -> None:
    """Attributes from a bot should be copied into a dictionary."""
    graph = SceneGraph()
    bot = ToyBot(graph)

    namespace = create_scripting_namespace(bot)

    assert namespace == {"rect": bot.rect}
