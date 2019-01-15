from shellshock.parse import Parseable, parse


class BoolOpType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
