from ...parse.tests import ParseTestCase


class TestInput(ParseTestCase):

    def test_input_with_target(self):
        """ Test that we can take user input to a variable """
        self.assert_parsed(
            """
import shellshock as ss
ss.input("What's your name? ", target='NAME')
print(NAME)
        """, """
read -p 'What'\\''s your name? ' NAME </dev/tty
echo -e $NAME
        """)

    def test_input_with_assignment(self):
        """ Test that we can take user input and assign it """
        self.assert_parsed(
            """
import shellshock as ss
NAME = ss.input("What's your name? ")
print(NAME)
        """, """
read -p 'What'\\''s your name? ' INPUT_VAR_93adc963 </dev/tty
NAME="$INPUT_VAR_93adc963"
echo -e $NAME
        """)
