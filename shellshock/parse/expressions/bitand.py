from shellshock.parse import Parseable, parse


class BitAndType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
