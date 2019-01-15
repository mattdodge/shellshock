from shellshock.parse import Parseable, parse


class UAddType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
