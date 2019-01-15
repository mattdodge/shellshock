from shellshock.parse import Parseable, parse


class StarredType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
