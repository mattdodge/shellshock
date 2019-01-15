from shellshock.parse import Parseable, parse


class IsNotType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
