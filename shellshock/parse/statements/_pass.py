from shellshock.parse import Parseable


class PassType(Parseable):

    @staticmethod
    def parse(obj):
        return ":"
