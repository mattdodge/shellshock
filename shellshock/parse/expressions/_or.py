from shellshock.parse import Parseable


class OrType(Parseable):

    @staticmethod
    def parse(obj):
        return "||"
