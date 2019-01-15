from shellshock.parse import Parseable, parse


class ReturnType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
