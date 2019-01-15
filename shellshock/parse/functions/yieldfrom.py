from shellshock.parse import Parseable, parse


class YieldFromType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
