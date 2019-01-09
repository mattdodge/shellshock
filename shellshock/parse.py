import ast
from .types.assign import convert as convert_assign
from .types.num import convert as convert_num
from .types.expr import convert as convert_expr
from .types.call import convert as convert_call
from .types.name import convert as convert_name
from .types.str import convert as convert_str


class Unparseable(Exception):
    pass

def parse_source(source_file):
    with open(source_file, 'r') as f:
        lines = f.readlines()
    return ast.parse("".join(lines)), lines


def convert_node(node):
    if isinstance(node, ast.Assign):
        return convert_assign(node)
    elif isinstance(node, ast.Num):
        return convert_num(node)
    elif isinstance(node, ast.Expr):
        return convert_expr(node)
    elif isinstance(node, ast.Call):
        return convert_call(node)
    elif isinstance(node, ast.Name):
        return convert_name(node)
    elif isinstance(node, ast.Str):
        return convert_str(node)

    raise Unparseable("Unknown type {}".format(node))


def convert_source(source_file):
    parsed, source_lines = parse_source(source_file)
    output = ""
    for node_idx, node in enumerate(parsed.body):
        this_node_line_no = node.lineno
        try:
            next_node_line_no = parsed.body[node_idx + 1].lineno
        except IndexError:
            next_node_line_no = len(source_lines) + 1

        output += "\n".join(
            ["# {}".format(line.rstrip('\n')) for line in source_lines[this_node_line_no - 1:next_node_line_no - 1]]) + "\n"
        
        try:
            node_out = convert_node(node)
        except Unparseable as e:
            node_out = "# Unknown parse of source code {}".format(e)

        if node_out:
            output += node_out + "\n" + "\n"
    return output
