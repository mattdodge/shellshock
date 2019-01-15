import ast


def get_parser(obj_type):
    """ Get a parser for a given obj_type """
    from shellshock.parse.types import (
        AssignType,
        CallType,
        NameType,
        NumType,
        StrType,
    )

    from shellshock.parse.expressions import (
        ExprType,
    )

    parse_mappings = {
        ast.Assign: AssignType,
        ast.Call: CallType,
        ast.Expr: ExprType,
        ast.Name: NameType,
        ast.Num: NumType,
        ast.Str: StrType,
    }

    if obj_type not in parse_mappings:
        raise Unparseable("Type {} not supported".format(obj_type))
    return parse_mappings[obj_type]


class Unparseable(Exception):
    pass


class Parseable():

    @staticmethod
    def parse(obj):
        raise NotImplemented


def parse(obj):
    try:
        node_out = get_parser(type(obj)).parse(obj)
    except Unparseable as e:
        node_out = "# Unknown parse of source code {}".format(e)

    return node_out
