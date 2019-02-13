from ...parse.tests import ParseTestCase


class TestFiles(ParseTestCase):

    def test_file_exists(self):
        self.assert_parsed(
            """
import shellshock as ss
if ss.file_exists('file'):
    pass
        """, """
if [ -e 'file' ]; then
  :
fi
        """)

    def test_file_is_file(self):
        self.assert_parsed(
            """
import shellshock as ss
if ss.file_is_file('file'):
    pass
        """, """
if [ -f 'file' ]; then
  :
fi
        """)

    def test_file_has_contents(self):
        self.assert_parsed(
            """
import shellshock as ss
if ss.file_has_contents('file'):
    pass
        """, """
if [ -s 'file' ]; then
  :
fi
        """)

    def test_file_is_dir(self):
        self.assert_parsed(
            """
import shellshock as ss
if ss.file_is_dir('file'):
    pass
        """, """
if [ -d 'file' ]; then
  :
fi
        """)

    def test_file_is_block(self):
        self.assert_parsed(
            """
import shellshock as ss
if ss.file_is_block('file'):
    pass
        """, """
if [ -b 'file' ]; then
  :
fi
        """)

    def test_file_is_character(self):
        self.assert_parsed(
            """
import shellshock as ss
if ss.file_is_character('file'):
    pass
        """, """
if [ -c 'file' ]; then
  :
fi
        """)

    def test_file_is_pipe(self):
        self.assert_parsed(
            """
import shellshock as ss
if ss.file_is_pipe('file'):
    pass
        """, """
if [ -p 'file' ]; then
  :
fi
        """)

    def test_file_is_symlink(self):
        self.assert_parsed(
            """
import shellshock as ss
if ss.file_is_symlink('file'):
    pass
        """, """
if [ -L 'file' ]; then
  :
fi
        """)

    def test_file_is_terminal(self):
        self.assert_parsed(
            """
import shellshock as ss
if ss.file_is_terminal('file'):
    pass
        """, """
if [ -t 'file' ]; then
  :
fi
        """)

    def test_file_has_read(self):
        self.assert_parsed(
            """
import shellshock as ss
if ss.file_has_read('file'):
    pass
        """, """
if [ -r 'file' ]; then
  :
fi
        """)

    def test_file_has_write(self):
        self.assert_parsed(
            """
import shellshock as ss
if ss.file_has_write('file'):
    pass
        """, """
if [ -w 'file' ]; then
  :
fi
        """)

    def test_file_has_execute(self):
        self.assert_parsed(
            """
import shellshock as ss
if ss.file_has_execute('file'):
    pass
        """, """
if [ -x 'file' ]; then
  :
fi
        """)
