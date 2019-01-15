from shellshock.parse import Parseable, parse


class UnaryOpType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
