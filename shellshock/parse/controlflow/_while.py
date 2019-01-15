from shellshock.parse import Parseable, parse


class WhileType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
