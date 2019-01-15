from shellshock.parse import Parseable, parse


class InType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
