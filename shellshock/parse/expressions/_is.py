from shellshock.parse import Parseable, parse


class IsType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
