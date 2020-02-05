"""Test toybot.scripting module."""
import json
from textwrap import dedent

from toybot.run.scripting import run


def test_toybot_script(capsys) -> None:
    """Render to the ConsoleRender to confirm commands are output as expected."""
    code = dedent(
        """\
        rect(0, 0, 100, 100)
        rect(25, 30, 50, 70)
        """
    )
    expected = [
        {"type": "path", "coords": [[0, 0], [0, 100], [100, 100], [100, 0]]},
        {"type": "path", "coords": [[25, 30], [25, 100], [75, 100], [75, 30]]},
    ]

    run(code)
    captured = capsys.readouterr()
    data = json.loads(captured.out)

    assert data == expected
