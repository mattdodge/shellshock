import ast
from .types.base import TypeInterface
from .exceptions import Unparseable


def parse_source(source_file):
    with open(source_file, 'r') as f:
        lines = f.readlines()
    return ast.parse("".join(lines)), lines


def convert_node(node):
    return TypeInterface.convert_node(node)


def convert_source(source_file, include_source=False):
    parsed, source_lines = parse_source(source_file)
    output = ""
    for node_idx, node in enumerate(parsed.body):

        if include_source:
            this_node_line_no = node.lineno
            try:
                next_node_line_no = parsed.body[node_idx + 1].lineno
            except IndexError:
                next_node_line_no = len(source_lines) + 1

            if next_node_line_no - this_node_line_no > 1:
                output += "\n".join([
                    ': \' (Multi-line original source)',
                ] + [
                    line.rstrip('\n') for line in source_lines[
                        this_node_line_no - 1:next_node_line_no - 1]
                ] + [
                    "\'",
                    ""
                ])
            else:
                output += "# Original source\n"
                output += "# {}".format(source_lines[this_node_line_no - 1])
        try:
            node_out = convert_node(node)
        except Unparseable as e:
            node_out = "# Unknown parse of source code {}".format(e)

        if node_out:
            output += node_out + "\n"
            if include_source:
                output += "\n"
    return output
