from shellshock.parse import Parseable, parse


class LtEType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
