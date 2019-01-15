from shellshock.parse import Parseable, parse


class withitemType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
