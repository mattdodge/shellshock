from shellshock.parse import Parseable, parse


class GtEType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
