from shellshock.parse import Parseable, parse


class AssertType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
