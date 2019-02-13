from shellshock.convert import ConvertContext
from ...parse.tests import ParseTestCase


class TestColors(ParseTestCase):

    def test_colors_active(self):
        self.assert_parsed(
            """
import shellshock as ss
print(ss.red("red"))
print(ss.cyan("cyan"))
print(ss.blue("blue"))
print(ss.yellow("yellow"))
print(ss.green("green"))
        """, """
echo -e "${SHELLSHOCK_COLOR_RC}red${SHELLSHOCK_COLOR_EC}"
echo -e "${SHELLSHOCK_COLOR_CC}cyan${SHELLSHOCK_COLOR_EC}"
echo -e "${SHELLSHOCK_COLOR_BC}blue${SHELLSHOCK_COLOR_EC}"
echo -e "${SHELLSHOCK_COLOR_YC}yellow${SHELLSHOCK_COLOR_EC}"
echo -e "${SHELLSHOCK_COLOR_GC}green${SHELLSHOCK_COLOR_EC}"
        """)
        # Make sure we declared that colors were used in our convert context
        self.assertTrue(ConvertContext.colors_used)

    def test_colors_inactive(self):
        self.assert_parsed(
            """
import shellshock as ss
        """, """
        """)
        # Make sure we didn't declare that colors were used
        self.assertFalse(ConvertContext.colors_used)
