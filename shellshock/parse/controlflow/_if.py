from ast import Name, Not, UnaryOp
from shellshock.parse import Parseable, parse
from shellshock.parse.body import parse_body


class IfType(Parseable):

    @classmethod
    def parse(cls, obj):
        out_lines = []
        out_lines.append(cls.parse_conditional(obj))
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
    def parse_conditional(cls, obj):
        if isinstance(obj.test, Name):
            # They are testing a boolean variable, compare to true
            return "if [ {test} = true ]; then".format(test=parse(obj.test))
        elif isinstance(obj.test, UnaryOp) and \
                isinstance(obj.test.op, Not) and \
                isinstance(obj.test.operand, Name):
            # They are testing NOT a boolean variable, still assume true
            return "if [ {test} = true ]; then".format(test=parse(obj.test))

        else:
            # It's a more complicated test, parse it
            return "if [ {test} ]; then".format(test=parse(obj.test))
