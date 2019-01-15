from shellshock.parse import Parseable, parse


class KeywordType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
