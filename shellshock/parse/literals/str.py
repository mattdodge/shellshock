from shellshock.parse import Parseable, parse


class StrType(Parseable):

    @staticmethod
    def parse(obj):
        return "'{}'".format(obj.s)
