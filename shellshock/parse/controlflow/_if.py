from shellshock.parse import Parseable, parse
from shellshock.parse.body import parse_body


class IfType(Parseable):

    @staticmethod
    def parse(obj):
        out_lines = []
        out_lines.append(
            "if [ {test} ]; then".format(test=parse(obj.test))
        )
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
