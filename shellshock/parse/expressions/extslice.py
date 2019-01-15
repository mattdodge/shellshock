from shellshock.parse import Parseable, parse


class ExtSliceType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
