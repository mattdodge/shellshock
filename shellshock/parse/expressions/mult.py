from shellshock.parse import Parseable, parse


class MultType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
