from shellshock.parse import Parseable, parse


class USubType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
