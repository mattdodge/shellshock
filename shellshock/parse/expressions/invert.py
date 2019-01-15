from shellshock.parse import Parseable, parse


class InvertType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
