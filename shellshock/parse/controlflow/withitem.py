from shellshock.parse import Parseable, parse


class WithitemType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
