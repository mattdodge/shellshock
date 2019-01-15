from shellshock.parse import Parseable, parse


class PowType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
