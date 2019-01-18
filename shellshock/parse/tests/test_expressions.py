from . import ParseTestCase


class TestExpressions(ParseTestCase):

    def test_basic_assign(self):
        self.assert_parsed(
            """
var = 5
        """, """
var=5
        """)

    def test_multiline_assign(self):
        self.assert_parsed(
            """
var = \
    5
        """, """
var=5
        """)

    def test_variable_access(self):
        self.assert_parsed(
            """
var = 5
print(var)
        """, """
var=5
echo $var
        """)

    def test_unknown_variable_access(self):
        self.assert_parsed_raises(
            """
print(var)
        """)
