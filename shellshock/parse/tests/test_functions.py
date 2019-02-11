from . import ParseTestCase


class TestFunctions(ParseTestCase):

    def test_print(self):
        self.assert_parsed(
            """
print('val')
        """, """
echo -e 'val'
        """)

    def test_print_var(self):
        self.assert_parsed(
            """
val = 1
print(val)
        """, """
val=1
echo -e $val
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

    def test_function_def(self):
        self.assert_parsed(
            """
def dosomething(var1, var2='default'):
    print(var1)
    print(var2)
dosomething('arg1', 'arg2')
        """, """
dosomething() {
  var1=${1}
  var2=${2:-'default'}
  echo -e $var1
  echo -e $var2
}
dosomething 'arg1' 'arg2'
        """)
