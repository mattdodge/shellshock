from shellshock.parse import Parseable, parse


class BitOrType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
