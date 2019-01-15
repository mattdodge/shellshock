from shellshock.parse import Parseable, parse


class PassType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
