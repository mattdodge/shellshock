from shellshock.parse import Parseable, parse


class AliasType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
