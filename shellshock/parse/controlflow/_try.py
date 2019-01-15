from shellshock.parse import Parseable, parse


class TryType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
