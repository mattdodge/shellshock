from shellshock.parse import Parseable, parse


class MatMultType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
