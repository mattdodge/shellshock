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

    def test_str(self):
        self.assert_parsed(
            """
var = "string stuff"
        """, """
var='string stuff'
        """)

    def test_str_single_quotes(self):
        """ Test that single quotes are escaped """
        self.assert_parsed(
            """
var = "my string's got stuff"
        """, """
var='my string'\\''s got stuff'
        """)
