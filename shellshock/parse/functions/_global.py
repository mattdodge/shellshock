from shellshock.parse import Parseable, parse


class GlobalType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
