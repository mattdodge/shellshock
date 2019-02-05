from os import getcwd, chdir
from os.path import join
from shellshock.convert import convert_source
from shutil import rmtree
import subprocess
import tempfile
from unittest import TestCase


class ShellshockTestCase(TestCase):

    _temp_dir = None
    _exec_dir = None
    _prev_dir = None
    _cleanup_file = True

    def setUp(self):
        super().setUp()
        if self._exec_dir is not None:
            self._prev_dir = getcwd()
            chdir(self._exec_dir)

    def tearDown(self):
        if self._prev_dir is not None:
            chdir(self._prev_dir)
        super().tearDown()

    def run_script(self, script_name):
        shell_script = convert_source(script_name)
        tmp = tempfile.mkdtemp(dir=self._temp_dir)
        script_file = join(tmp, "script_{}.sh".format(self._testMethodName))
        with open(script_file, 'w+') as script_fd:
            script_fd.write(shell_script)

        # subprocess.run('/bin/bash {}'.format(script_file))
        result = subprocess.run(
            ['/bin/bash', script_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if self._cleanup_file:
            rmtree(tmp)
        return result