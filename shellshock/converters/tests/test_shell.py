from shellshock.convert import ConvertContext
from ...parse.tests import ParseTestCase


class TestShell(ParseTestCase):

    def test_shebang_anywhere(self):
        """ Shebangs anywhere reset the convert context """
        self.assert_parsed(
            """
import shellshock as ss
print('value')
ss.shebang('newshebang')
        """, """
echo -e 'value'
        """)
        self.assertEqual(ConvertContext.shebang, 'newshebang')

    def test_exit(self):
        self.assert_parsed(
            """
import shellshock as ss
ss.exit(5)
        """, """
exit 5
        """)

    def test_subshell(self):
        self.assert_parsed(
            """
import shellshock as ss
print(ss.subshell('whoami'))
        """, """
echo -e $(whoami)
        """)
