from shellshock.parse import Parseable, parse


class ListType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
