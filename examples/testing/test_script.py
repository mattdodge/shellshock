from os.path import join, dirname
from shellshock.testing.test_case import ShellshockTestCase


# Shellshock test cases should extend ShellshockTestCase
class TestScript(ShellshockTestCase):

    # Set this to False to not delete the temporary script after the test run
    _cleanup_file = False

    # Where to create the temporary shell script for the test
    _temp_dir = dirname(__file__)

    def test_basic_function(self):
        # Run the "script.py" script that exists in this folder
        out = self.run_script(join(dirname(__file__), 'script.py'))
        # Make sure our output looks like we want it to
        self.assertIn(b'3\n10\n', out.stdout)
        # And nothing should be on stderr
        self.assertEqual(b'', out.stderr)

    def test_mocking_method(self):
        mock_call = self.add_mock_function('funccall', side_effect="ss.noop()")
        out = self.run_script(join(dirname(__file__), 'script.py'))
        # Mock arguments are always strings
        mock_call.assert_called_once_with('3')
        # Since we mocked our method we shouldn't actually see any output
        self.assertNotIn(b'3', out.stdout)

    def test_mock_return_true(self):
        # Make our command check return true
        mock_call = self.add_mock_function('command_exists', side_effect="True")
        out = self.run_script(join(dirname(__file__), 'script.py'))
        self.assertIn(b'Command exists', out.stdout)

    def test_mock_return_false(self):
        # Make our command check return false
        mock_call = self.add_mock_function('command_exists', side_effect="False")
        out = self.run_script(join(dirname(__file__), 'script.py'))
        self.assertIn(b'Command doesnt exist', out.stdout)
