from shellshock.parse import Parseable, parse


class EllipsisType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
