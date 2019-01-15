from shellshock.parse import Parseable, parse


class TryExceptType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
