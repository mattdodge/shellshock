from shellshock.parse import Parseable


class StrType(Parseable):

    @staticmethod
    def parse(obj):
        return "'{}'".format(obj.s)
