from shellshock.parse import Parseable, parse


class ForType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
