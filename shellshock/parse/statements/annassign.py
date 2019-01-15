from shellshock.parse import Parseable, parse


class AnnAssignType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
