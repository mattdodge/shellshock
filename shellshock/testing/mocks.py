import ast
from shellshock.parse import Parseable, parse
from shellshock.parse.body import parse_body
from unittest.mock import Mock


def get_testing_mocks():
    """ Return function definitions for mocked calls """
    if len(Parseable._known_mocks) == 0:
        return ""
    out = []
    out.append("__record_mock_call() {")
    out.append("echo $@ >> __mocks")
    out.append("}")
    for mock_call, mock in Parseable._known_mocks.items():
        out.append("__mock_{}() {{".format(mock_call))
        out.append(mock.side_effect)
        out.append("}}".format(mock_call))
    # Add two extra newlines for readability
    out.append("")
    out.append("")
    return "\n".join(out)


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
