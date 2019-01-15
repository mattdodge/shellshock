from shellshock.parse import Parseable, parse


class ContinueType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
