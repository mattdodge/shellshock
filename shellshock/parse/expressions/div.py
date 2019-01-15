from shellshock.parse import Parseable, parse


class DivType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
