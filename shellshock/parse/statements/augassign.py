from shellshock.parse import Parseable, parse


class AugAssignType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
