from shellshock.parse import Parseable, parse


class NotInType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
