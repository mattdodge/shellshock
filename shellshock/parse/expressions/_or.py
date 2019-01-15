from shellshock.parse import Parseable, parse


class OrType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
