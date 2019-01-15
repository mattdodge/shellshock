import ast


def get_parser(obj_type):
    """ Get a parser for a given obj_type """
    from shellshock.parse.types import (
        AssignType,
        CallType,
    )

    import shellshock.parse.literals as literals
    import shellshock.parse.variables as variables
    import shellshock.parse.expressions as expressions

    parse_mappings = {
        ast.Num: literals.NumType,
        ast.Str: literals.StrType,
        ast.FormattedValue: literals.FormattedValueType,
        ast.JoinedStr: literals.JoinedStrType,
        ast.Bytes: literals.BytesType,
        ast.List: literals.ListType,
        ast.Tuple: literals.TupleType,
        ast.Set: literals.SetType,
        ast.Dict: literals.DictType,
        ast.Ellipsis: literals.EllipsisType,
        ast.NameConstant: literals.NameConstantType,

        ast.Name: variables.NameType,
        ast.Load: variables.LoadType,
        ast.Store: variables.StoreType,
        ast.Del: variables.DelType,
        ast.Starred: variables.StarredType,

        ast.Expr: expressions.ExprType,
        ast.Expr: expressions.ExprType,
        ast.UnaryOp: expressions.UnaryOpType,
        ast.UAdd: expressions.UAddType,
        ast.USub: expressions.USubType,
        ast.Not: expressions.NotType,
        ast.Invert: expressions.InvertType,
        ast.BinOp: expressions.BinOpType,
        ast.Add: expressions.AddType,
        ast.Sub: expressions.SubType,
        ast.Mult: expressions.MultType,
        ast.Div: expressions.DivType,
        ast.FloorDiv: expressions.FloorDivType,
        ast.Mod: expressions.ModType,
        ast.Pow: expressions.PowType,
        ast.LShift: expressions.LShiftType,
        ast.RShift: expressions.RShiftType,
        ast.BitOr: expressions.BitOrType,
        ast.BitXor: expressions.BitXorType,
        ast.BitAnd: expressions.BitAndType,
        ast.MatMult: expressions.MatMultType,
        ast.BoolOp: expressions.BoolOpType,
        ast.And: expressions.AndType,
        ast.Or: expressions.OrType,
        ast.Compare: expressions.CompareType,
        ast.Eq: expressions.EqType,
        ast.NotEq: expressions.NotEqType,
        ast.Lt: expressions.LtType,
        ast.LtE: expressions.LtEType,
        ast.Gt: expressions.GtType,
        ast.GtE: expressions.GtEType,
        ast.Is: expressions.IsType,
        ast.IsNot: expressions.IsNotType,
        ast.In: expressions.InType,
        ast.NotIn: expressions.NotInType,
        ast.Call: expressions.CallType,
        ast.keyword: expressions.KeywordType,
        ast.IfExp: expressions.IfExpType,
        ast.Attribute: expressions.AttributeType,
        ast.Subscript: expressions.SubscriptType,
        ast.Index: expressions.IndexType,
        ast.Slice: expressions.SliceType,
        ast.ExtSlice: expressions.ExtSliceType,
        ast.ListComp: expressions.ListCompType,
        ast.SetComp: expressions.SetCompType,
        ast.GeneratorExp: expressions.GeneratorExpType,
        ast.DictComp: expressions.DictCompType,
        ast.comprehension: expressions.ComprehensionType,

        ast.Assign: AssignType,
    }

    if obj_type not in parse_mappings:
        raise Unparseable("Type {} not supported".format(obj_type))
    return parse_mappings[obj_type]


class Unparseable(Exception):
    pass


class Parseable():

    @staticmethod
    def parse(obj):
        raise NotImplementedError


def parse(obj):
    try:
        node_out = get_parser(type(obj)).parse(obj)
    except Unparseable as e:
        node_out = "# Unknown parse of source code {}".format(e)

    return node_out
