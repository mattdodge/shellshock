from ...parse.tests import ParseTestCase


class TestInput(ParseTestCase):

    def test_input(self):
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
