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

    def test_if_boolean(self):
        """ Tests we can check a boolean in an if """
        self.assert_parsed(
            """
bool_var = True
if bool_var:
    print("here")
if bool_var == 5:
    print("again")
        """, """
bool_var=true
if [ $bool_var = true ]; then
  echo -e 'here'
fi
if [ $bool_var -eq 5 ]; then
  echo -e 'again'
fi
        """)

    def test_if_not(self):
        """ Tests we can check the inverse of a boolean """
        self.assert_parsed(
            """
bool_var = True
if not bool_var:
    print("here")
        """, """
bool_var=true
if [ ! $bool_var = true ]; then
  echo -e 'here'
fi
        """)

    def test_if_and(self):
        """ Tests and conditions in an if statement """
        self.assert_parsed(
            """
bool_var = True
another_var = False
if bool_var and not another_var:
    print("here")
        """, """
bool_var=true
another_var=false
if [ $bool_var = true ] && [ ! $another_var = true ]; then
  echo -e 'here'
fi
        """)

    def test_if_or(self):
        """ Tests or conditions in an if statement """
        self.assert_parsed(
            """
bool_var = True
another_var = False
if bool_var or not another_var:
    print("here")
        """, """
bool_var=true
another_var=false
if [ $bool_var = true ] || [ ! $another_var = true ]; then
  echo -e 'here'
fi
        """)
