from shellshock.parse import Parseable, parse


class IndexType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
