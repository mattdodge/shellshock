from shellshock.parse import Parseable, parse


class ArgType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
