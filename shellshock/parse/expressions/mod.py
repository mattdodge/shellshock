from shellshock.parse import Parseable, parse


class ModType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
