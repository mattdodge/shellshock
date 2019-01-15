from shellshock.parse import Parseable, parse


class TryFinallyType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
