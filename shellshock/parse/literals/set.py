from shellshock.parse import Parseable, parse


class SetType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
