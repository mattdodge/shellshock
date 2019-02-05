from . import ParseTestCase


class TestFunctions(ParseTestCase):

    def test_true(self):
        self.assert_parsed(
            """
True
        """, """
true
        """)

    def test_false(self):
        self.assert_parsed(
            """
False
        """, """
false
        """)

    def test_none(self):
        self.assert_parsed(
            """
None
        """, """
none
        """)
