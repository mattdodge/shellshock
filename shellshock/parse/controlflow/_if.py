from shellshock.parse import Parseable, parse


class IfType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
