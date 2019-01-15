from shellshock.parse import Parseable, parse


class SliceType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
