from shellshock.parse import Parseable, parse
from shellshock.parse.body import parse_body


class IfType(Parseable):

    @staticmethod
    def parse(obj):
        return [
            "if [ {test} ]; then".format(test=parse(obj.test)),
            "{body}".format(body=parse_body(obj.body)),
            "fi",
        ]
