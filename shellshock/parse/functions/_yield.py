from shellshock.parse import Parseable, parse


class YieldType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
