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
  echo -e 'here'
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
  echo -e 'here'
  echo -e 'and here'
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
    echo -e 'here'
  fi
fi
        """)

    def test_else(self):
        self.assert_parsed(
            """
var = "value"
if var == "value":
    print("here")
else:
    print("not here")
        """, """
var='value'
if [ $var == 'value' ]; then
  echo -e 'here'
else
  echo -e 'not here'
fi
        """)

    def test_elif(self):
        """ Elifs are nested, no elseif support """
        self.assert_parsed(
            """
var = "value"
if var == "value":
    print("here")
elif var == "other":
    print("and here")
else:
    print("not here")
        """, """
var='value'
if [ $var == 'value' ]; then
  echo -e 'here'
else
  if [ $var == 'other' ]; then
    echo -e 'and here'
  else
    echo -e 'not here'
  fi
fi
        """)
