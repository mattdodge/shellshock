from . import ParseTestCase


class TestStatements(ParseTestCase):

    def test_pass(self):
        self.assert_parsed(
            """
pass
        """, """
:
        """)
