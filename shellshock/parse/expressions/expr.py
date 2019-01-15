from shellshock.parse import Parseable, parse


class ExprType(Parseable):

    @staticmethod
    def parse(obj):
        return parse(obj.value)
