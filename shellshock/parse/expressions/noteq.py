from shellshock.parse import Parseable, parse


class NotEqType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
