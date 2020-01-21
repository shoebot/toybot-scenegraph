from textwrap import dedent

from toybot.run.scripting import run


def test_toybot_script(capsys):
    """
    Small end to end test using the ConsoleRender to confirm commands get rendered.
    """
    code = dedent(
        """\
        rect(0, 0, 100, 100)
        rect(25, 30, 50, 70)
        """
    )
    expected = dedent(
        """\
        {'type': 'path', 'coords': [(0, 0), (0, 100), (100, 100), (100, 0)]}
        {'type': 'path', 'coords': [(25, 30), (25, 100), (75, 100), (75, 30)]}
        """
    )

    run(code)
    captured = capsys.readouterr()

    assert captured.out == expected
