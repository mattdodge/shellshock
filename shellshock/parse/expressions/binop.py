from shellshock.parse import Parseable, parse


class BinOpType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
