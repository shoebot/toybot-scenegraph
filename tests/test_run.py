from toybot.languages.toybot import ToyBot
from toybot.run.scripting import create_scripting_namespace
from toybot.scenegraph.scenegraph import SceneGraph


def test_create_scripting_namespace():
    graph = SceneGraph()
    bot = ToyBot(graph)

    namespace = create_scripting_namespace(bot)

    assert namespace == {"rect": bot.rect}
