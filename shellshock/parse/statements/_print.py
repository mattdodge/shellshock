from shellshock.parse import Parseable, parse


class PrintType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
