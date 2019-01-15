from shellshock.parse import Parseable, parse


class Type(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplemented
