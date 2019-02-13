from shellshock.parse import Parseable, parse


class UnaryOpType(Parseable):

    @staticmethod
    def parse(obj):
        return "{} {}".format(
            parse(obj.op),
            parse(obj.operand),
        )
