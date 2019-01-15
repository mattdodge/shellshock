from shellshock.parse import Parseable, parse


class WithType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
