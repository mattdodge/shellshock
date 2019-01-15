from shellshock.parse import Parseable, parse


class ListCompType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
