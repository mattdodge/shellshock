from ast import Name, Not, UnaryOp, BoolOp
from shellshock.parse import Parseable, parse
from shellshock.parse.body import parse_body


class IfType(Parseable):

    @classmethod
    def parse(cls, obj):
        out_lines = []

        if isinstance(obj.test, BoolOp):
            conds = " {} ".format(parse(obj.test.op)).join(
                [cls.parse_conditional(val) for val in obj.test.values])
        else:
            conds = cls.parse_conditional(obj.test)
        out_lines.append("if {conds}; then".format(conds=conds))
        out_lines.append(
            "{body}".format(body=parse_body(obj.body))
        )
        if obj.orelse:
            out_lines.append("else")
            out_lines.append(
                "{body}".format(body=parse_body(obj.orelse))
            )
        out_lines.append("fi")
        return out_lines

    @classmethod
    def parse_conditional(cls, obj_test):
        if isinstance(obj_test, Name):
            # They are testing a boolean variable, compare to true
            return "[ {test} = true ]".format(test=parse(obj_test))
        elif isinstance(obj_test, UnaryOp) and \
                isinstance(obj_test.op, Not) and \
                isinstance(obj_test.operand, Name):
            # They are testing NOT a boolean variable, still assume true
            return "[ {test} = true ]".format(test=parse(obj_test))

        else:
            # It's a more complicated test, parse it
            return "[ {test} ]".format(test=parse(obj_test))
