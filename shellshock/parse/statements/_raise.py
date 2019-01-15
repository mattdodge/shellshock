from shellshock.parse import Parseable, parse


class RaiseType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
