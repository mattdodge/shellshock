from ast import Add
from shellshock.parse import Parseable, parse, Unparseable


class BinOpType(Parseable):

    @classmethod
    def parse(cls, obj):
        if cls.is_numeric(obj.left) and cls.is_numeric(obj.right):
            return cls.numeric_bin_op(obj)
        else:
            return cls.string_bin_op(obj)

    @classmethod
    def numeric_bin_op(cls, obj):
        return "$(({left} {op} {right}))".format(
            left=parse(obj.left),
            op=parse(obj.op),
            right=parse(obj.right)
        )

    @classmethod
    def string_bin_op(cls, obj):
        if not isinstance(obj.op, Add):
            raise Unparseable("Binary op {} not supported on strings".format(
                type(obj.op)))

        return "{}{}".format(parse(obj.left), parse(obj.right))
