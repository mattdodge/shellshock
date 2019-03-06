from os.path import join
from shellshock.convert import convert_source, load_converters
from shellshock.parse import Parseable
from shellshock.testing.mocks import TestingMock, parse_mocks
from shutil import rmtree
import subprocess
import tempfile
from unittest import TestCase


class ShellshockTestCase(TestCase):

    _temp_dir = None
    _exec_dir = None
    _cleanup_file = True

    def setUp(self):
        super().setUp()
        Parseable._known_refs.add("ss")
        load_converters()
        self.mocks = {}

    def tearDown(self):
        super().tearDown()

    def run_script(self, script_name):
        shell_script = convert_source(script_name)
        tmp = tempfile.mkdtemp(dir=self._temp_dir)
        script_file = join(tmp, "script_{}.sh".format(self._testMethodName))
        with open(script_file, 'w+') as script_fd:
            script_fd.write(shell_script)
        exec_dir = self._exec_dir if self._exec_dir is not None else tmp

        result = subprocess.run(
            ['/bin/bash', script_file],
            cwd=exec_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        # Go through the called mocks and actually "call" them
        parse_mocks(cwd=exec_dir)
        if self._cleanup_file:
            rmtree(tmp)
        return result

    def add_mock_function(self, function_call_id, side_effect=None):
        self.mocks[function_call_id] = TestingMock(side_effect=side_effect)
        Parseable._known_mocks = self.mocks
        return self.mocks[function_call_id].mock
