from shellshock.parse import Parseable, parse


class ArgumentsType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
