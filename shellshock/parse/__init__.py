import ast


class Unparseable(Exception):
    pass


class Parseable():

    @staticmethod
    def parse(obj):
        raise NotImplementedError


def parse(obj):
    try:
        node_out = __get_parser(type(obj)).parse(obj)
    except Unparseable as e:
        node_out = "# Unknown parse of source code {}".format(e)

    return node_out


def __get_parser(obj_type):
    """ Get a parser for a given obj_type """
    import shellshock.parse.literals as literals
    import shellshock.parse.variables as variables
    import shellshock.parse.expressions as expressions
    import shellshock.parse.statements as statements

    def get_ast_type(ast_type):
        return getattr(ast, ast_type, "Unknown{}".format(ast_type))

    parse_mappings = {
        get_ast_type('Num'): literals.NumType,
        get_ast_type('Str'): literals.StrType,
        get_ast_type('FormattedValue'): literals.FormattedValueType,
        get_ast_type('JoinedStr'): literals.JoinedStrType,
        get_ast_type('Bytes'): literals.BytesType,
        get_ast_type('List'): literals.ListType,
        get_ast_type('Tuple'): literals.TupleType,
        get_ast_type('Set'): literals.SetType,
        get_ast_type('Dict'): literals.DictType,
        get_ast_type('Ellipsis'): literals.EllipsisType,
        get_ast_type('NameConstant'): literals.NameConstantType,

        get_ast_type('Name'): variables.NameType,
        get_ast_type('Load'): variables.LoadType,
        get_ast_type('Store'): variables.StoreType,
        get_ast_type('Del'): variables.DelType,
        get_ast_type('Starred'): variables.StarredType,

        get_ast_type('Expr'): expressions.ExprType,
        get_ast_type('Expr'): expressions.ExprType,
        get_ast_type('UnaryOp'): expressions.UnaryOpType,
        get_ast_type('UAdd'): expressions.UAddType,
        get_ast_type('USub'): expressions.USubType,
        get_ast_type('Not'): expressions.NotType,
        get_ast_type('Invert'): expressions.InvertType,
        get_ast_type('BinOp'): expressions.BinOpType,
        get_ast_type('Add'): expressions.AddType,
        get_ast_type('Sub'): expressions.SubType,
        get_ast_type('Mult'): expressions.MultType,
        get_ast_type('Div'): expressions.DivType,
        get_ast_type('FloorDiv'): expressions.FloorDivType,
        get_ast_type('Mod'): expressions.ModType,
        get_ast_type('Pow'): expressions.PowType,
        get_ast_type('LShift'): expressions.LShiftType,
        get_ast_type('RShift'): expressions.RShiftType,
        get_ast_type('BitOr'): expressions.BitOrType,
        get_ast_type('BitXor'): expressions.BitXorType,
        get_ast_type('BitAnd'): expressions.BitAndType,
        get_ast_type('MatMult'): expressions.MatMultType,
        get_ast_type('BoolOp'): expressions.BoolOpType,
        get_ast_type('And'): expressions.AndType,
        get_ast_type('Or'): expressions.OrType,
        get_ast_type('Compare'): expressions.CompareType,
        get_ast_type('Eq'): expressions.EqType,
        get_ast_type('NotEq'): expressions.NotEqType,
        get_ast_type('Lt'): expressions.LtType,
        get_ast_type('LtE'): expressions.LtEType,
        get_ast_type('Gt'): expressions.GtType,
        get_ast_type('GtE'): expressions.GtEType,
        get_ast_type('Is'): expressions.IsType,
        get_ast_type('IsNot'): expressions.IsNotType,
        get_ast_type('In'): expressions.InType,
        get_ast_type('NotIn'): expressions.NotInType,
        get_ast_type('Call'): expressions.CallType,
        get_ast_type('keyword'): expressions.KeywordType,
        get_ast_type('IfExp'): expressions.IfExpType,
        get_ast_type('Attribute'): expressions.AttributeType,
        get_ast_type('Subscript'): expressions.SubscriptType,
        get_ast_type('Index'): expressions.IndexType,
        get_ast_type('Slice'): expressions.SliceType,
        get_ast_type('ExtSlice'): expressions.ExtSliceType,
        get_ast_type('ListComp'): expressions.ListCompType,
        get_ast_type('SetComp'): expressions.SetCompType,
        get_ast_type('GeneratorExp'): expressions.GeneratorExpType,
        get_ast_type('DictComp'): expressions.DictCompType,
        get_ast_type('comprehension'): expressions.ComprehensionType,

        get_ast_type('Assign'): statements.AssignType,
        get_ast_type('AnnAssign'): statements.AnnAssignType,
        get_ast_type('AugAssign'): statements.AugAssignType,
        get_ast_type('Print'): statements.PrintType,
        get_ast_type('Raise'): statements.RaiseType,
        get_ast_type('Assert'): statements.AssertType,
        get_ast_type('Delete'): statements.DeleteType,
        get_ast_type('Pass'): statements.PassType,
        get_ast_type('Import'): statements.ImportType,
        get_ast_type('ImportFrom'): statements.ImportFromType,
        get_ast_type('alias'): statements.AliasType,

    }

    if obj_type not in parse_mappings:
        raise Unparseable("Type {} not supported".format(obj_type))
    return parse_mappings[obj_type]
