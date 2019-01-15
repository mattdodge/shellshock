from shellshock.parse import Parseable, parse


class BitXorType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
