from shellshock.parse import Parseable, parse


class IfExpType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
