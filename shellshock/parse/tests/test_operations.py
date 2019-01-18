from . import ParseTestCase


class TestOperations(ParseTestCase):

    def test_if(self):
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

    def test_if_multiline_body(self):
        self.assert_parsed(
            """
var = "value"
if var == "value":
    print("here")
    print("and here")
        """, """
var='value'
if [ $var == 'value' ]; then
  echo 'here'
  echo 'and here'
fi
        """)

    def test_nested_if(self):
        self.assert_parsed(
            """
var = "value"
if var == "value":
    if var == "value":
        print("here")
        """, """
var='value'
if [ $var == 'value' ]; then
  if [ $var == 'value' ]; then
    echo 'here'
  fi
fi
        """)
