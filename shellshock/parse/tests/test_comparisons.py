from . import ParseTestCase


class TestComparisons(ParseTestCase):

    def test_str_eq(self):
        self.assert_parsed(
            """
var = "value"
if var == "value":
    print("here")
        """, """
var='value'
if [ $var == 'value' ]; then
  echo 'here'
fi
        """)

    def test_str_not_eq(self):
        self.assert_parsed(
            """
var = "value"
if var != "value":
    print("here")
        """, """
var='value'
if [ $var != 'value' ]; then
  echo 'here'
fi
        """)

    def test_str_less(self):
        self.assert_parsed(
            """
var = "value"
if var < "value":
    print("here")
        """, """
var='value'
if [ $var \\< 'value' ]; then
  echo 'here'
fi
        """)

    def test_str_less_eq(self):
        self.assert_parsed_raises(
            """
var = "value"
if var <= "value":
    print("here")
        """)

    def test_str_greater(self):
        self.assert_parsed(
            """
var = "value"
if var > "value":
    print("here")
        """, """
var='value'
if [ $var \\> 'value' ]; then
  echo 'here'
fi
        """)

    def test_str_greater_eq(self):
        self.assert_parsed_raises(
            """
var = "value"
if var >= "value":
    print("here")
        """)

    def test_numeric_eq(self):
        self.assert_parsed(
            """
var = "3"
if var == 3:
    print("here")
        """, """
var='3'
if [ $var -eq 3 ]; then
  echo 'here'
fi
        """)

    def test_numeric_not_eq(self):
        self.assert_parsed(
            """
var = "3"
if var != 3:
    print("here")
        """, """
var='3'
if [ $var -ne 3 ]; then
  echo 'here'
fi
        """)

    def test_numeric_less(self):
        self.assert_parsed(
            """
var = "3"
if var < 3:
    print("here")
        """, """
var='3'
if [ $var -lt 3 ]; then
  echo 'here'
fi
        """)

    def test_numeric_less_eq(self):
        self.assert_parsed(
            """
var = "3"
if var <= 3:
    print("here")
        """, """
var='3'
if [ $var -le 3 ]; then
  echo 'here'
fi
        """)

    def test_numeric_greater(self):
        self.assert_parsed(
            """
var = "3"
if var > 3:
    print("here")
        """, """
var='3'
if [ $var -gt 3 ]; then
  echo 'here'
fi
        """)

    def test_numeric_greater_eq(self):
        self.assert_parsed(
            """
var = "3"
if var >= 3:
    print("here")
        """, """
var='3'
if [ $var -ge 3 ]; then
  echo 'here'
fi
        """)
