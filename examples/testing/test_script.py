from os.path import join, dirname
from shellshock.testing.test_case import ShellshockTestCase


# Shellshock test cases should extend ShellshockTestCase
class TestScript(ShellshockTestCase):

    # Set this to False to not delete the temporary script after the test run
    _cleanup_file = True

    # Where to create the temporary shell script for the test
    _temp_dir = dirname(__file__)

    def test_it(self):
        # Run the "script.py" script that exists in this folder
        out = self.run_script(join(dirname(__file__), 'script.py'))
        # Make sure our output looks like we want it to
        self.assertEqual(b'3\n10\n', out.stdout)
        # And nothing should be on stderr
        self.assertEqual(b'', out.stderr)
