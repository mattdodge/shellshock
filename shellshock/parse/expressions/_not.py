from shellshock.parse import Parseable, parse


class NotType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
