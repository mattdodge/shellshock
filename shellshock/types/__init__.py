def get_types():
    from .assign import AssignType
    from .call import CallType
    from .expr import ExprType
    from .name import NameType
    from .num import NumType
    from .str import StrType

    return [
        AssignType,
        CallType,
        ExprType,
        NameType,
        NumType,
        StrType,
    ]
