from shellshock.parse import Parseable, parse


class EqType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
