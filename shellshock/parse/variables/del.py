from shellshock.parse import Parseable, parse


class DelType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
