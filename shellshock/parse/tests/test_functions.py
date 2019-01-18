from . import ParseTestCase


class TestFunctions(ParseTestCase):

    def test_print(self):
        self.assert_parsed(
            """
print('val')
        """, """
echo 'val'
        """)

    def test_print_var(self):
        self.assert_parsed(
            """
val = 1
print(val)
        """, """
val=1
echo $val
        """)

    def test_raw_shell(self):
        self.assert_parsed(
            """
import shellshock as ss
ss.shell('touch testfile')
        """, """
touch testfile
        """)

    def test_raw_shell_multiline(self):
        self.assert_parsed(
            """
import shellshock as ss
ss.shell(\"\"\"
touch testfile
touch anotherone
\"\"\")
        """, """
touch testfile
touch anotherone
        """)
