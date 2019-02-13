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
echo -e $var
        """)

    def test_unknown_variable_access(self):
        self.assert_parsed_raises(
            """
print(var)
        """)

    def test_string_concat(self):
        self.assert_parsed(
            """
var = "st1" + "st2"
print(var)
        """, """
var='st1''st2'
echo -e $var
        """)

    def test_numeric_add(self):
        self.assert_parsed(
            """
var = 5 + 3
print(var)
        """, """
var=$((5 + 3))
echo -e $var
        """)

    def test_add_num_and_string(self):
        """ Make sure if a number is "+"ed to a string it's a concat """
        self.assert_parsed(
            """
var = 5 + 'string'
print(var)
        """, """
var=5'string'
echo -e $var
        """)
