from shellshock.parse import Parseable, parse
from shellshock.parse.body import parse_body


class FunctionDefType(Parseable):

    @classmethod
    def parse(cls, obj):
        cls._known_funcs.add(obj.name)
        return "\n".join([
            "{}() {{".format(obj.name),
            parse(obj.args),
            parse_body(obj.body),
            "}",
        ])
