from shellshock.parse import Parseable, parse


class GeneratorExpType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
