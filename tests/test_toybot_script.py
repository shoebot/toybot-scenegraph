from textwrap import dedent

from toybot.languages.helpers import run


def test_toybot_script():
    """
    Small end to end test.
    """
    code = dedent(
        """
        rect(0, 0, 100, 100)
        rect(25, 30, 50, 70)
        """
    )

    run(code)
