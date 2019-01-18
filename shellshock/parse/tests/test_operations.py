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
