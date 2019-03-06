import ast
from os import getcwd
from os.path import join, isfile
from shellshock.parse import Parseable, parse
from shellshock.parse.body import parse_body
from unittest.mock import Mock


_MOCKS_FILENAME = "__mocks"


def get_testing_mocks():
    """ Return function definitions for mocked calls """
    if len(Parseable._known_mocks) == 0:
        return ""
    out = []
    out.append("__record_mock_call() {")
    out.append("  echo $@ >> " + _MOCKS_FILENAME)
    out.append("}")
    for mock_call, mock in Parseable._known_mocks.items():
        out.append("__mock_{}() {{".format(mock_call))
        out.append("  " + mock.side_effect)
        out.append("}}".format(mock_call))
    # Add two extra newlines for readability
    out.append("")
    out.append("")
    return "\n".join(out)


def parse_mocks(cwd=None):
    """ Read the __mocks file and figure out which mocks were called.
    
    Args:
        cwd - The working directory where the mocks file will be
    """
    if not Parseable._known_mocks:
        return
    if cwd is None:
        cwd = getcwd()
    mocks_file = join(cwd, _MOCKS_FILENAME)
    if not isfile(mocks_file):
        return
    with open(mocks_file) as mock_calls:
        for mock_call in mock_calls.readlines():
            mock_call = mock_call.strip()  # remove trailing newline
            args = mock_call.split(" ")  # TODO: Handle quotes
            # TODO: Handle kwargs
            Parseable._known_mocks[args[0]].mock(*args[1:])


class TestingMock():

    def __init__(self, mock=None, side_effect=None):
        if mock is not None:
            self.mock = mock
        else:
            self.mock = Mock()
        if side_effect is not None:
            self.side_effect_src = side_effect
        else:
            self.side_effect_src = "ss.noop()"
        self.side_effect = parse_body(ast.parse(self.side_effect_src).body)
