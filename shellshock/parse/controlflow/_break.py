from shellshock.parse import Parseable, parse


class BreakType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
