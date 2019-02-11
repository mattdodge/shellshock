from shellshock.parse.body import parse_body
from shellshock.testing.mocks import get_testing_mocks
from shellshock.converters.colors import _get_color_init
import ast
import sys


class ConvertContext(object):
    include_source = False
    allow_errors = False
    colors_used = False
    indent_level = 0
    lines = []

    @classmethod
    def get_line(cls, node):
        """ Get the source line for a node """
        return cls.lines[node.lineno - 1].strip()

    @classmethod
    def reset(cls):
        cls.include_source = False
        cls.allow_errors = False
        cls.colors_used = False
        cls.indent_level = 0
        cls.shebang = '#!/bin/bash'
        cls.lines = []


def load_converters(custom_converters=[]):
    # Known converters
    import shellshock.converters.ops  # noqa
    import shellshock.converters.shell  # noqa
    import shellshock.converters.colors  # noqa

    for custom in custom_converters:
        try:
            __import__(custom)
        except (ModuleNotFoundError, ImportError):
            print("FATAL: Invalid custom converter specified : {}".format(custom))  # noqa
            sys.exit(1)


def convert_source(source_file, include_source=False, allow_errors=False):
    ConvertContext.include_source = include_source
    ConvertContext.allow_errors = allow_errors
    with open(source_file, 'r') as f:
        lines = f.readlines()
    ConvertContext.lines = lines
    body = ConvertContext.shebang + "\n"
    body += get_testing_mocks()
    parsed = parse_body(ast.parse("".join(lines)).body)
    if ConvertContext.colors_used:
        body += _get_color_init()
    body += parsed
    return body
