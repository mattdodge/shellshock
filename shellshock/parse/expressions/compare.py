from shellshock.parse import Parseable, parse


class CompareType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
