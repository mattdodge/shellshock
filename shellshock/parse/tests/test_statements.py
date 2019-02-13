from . import ParseTestCase


class TestStatements(ParseTestCase):

    def test_pass(self):
        self.assert_parsed(
            """
pass
        """, """
:
        """)

    def test_assign_from_input(self):
        """ Test that we can assign from user input """
        self.assert_parsed(
            """
my_input = ss.input('who are you? ')
print(my_input)
        """, """
read -p 'who are you? ' INPUT_VAR_9da277c0 </dev/tty
my_input="$INPUT_VAR_9da277c0"
echo -e $my_input
        """)
