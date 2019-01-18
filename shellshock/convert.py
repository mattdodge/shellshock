from shellshock.parse.body import parse_body
import ast


class ConvertContext(object):
    include_source = False
    allow_errors = False
    indent_level = 0
    lines = []

    @classmethod
    def get_line(cls, node):
        """ Get the source line for a node """
        return cls.lines[node.lineno - 1].strip()


def convert_source(source_file, include_source=False, allow_errors=False):
    ConvertContext.include_source = include_source
    ConvertContext.allow_errors = allow_errors
    with open(source_file, 'r') as f:
        lines = f.readlines()
    ConvertContext.lines = lines
    return parse_body(ast.parse("".join(lines)).body)
