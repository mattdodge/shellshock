from shellshock.parse import Parseable, parse


class StrType(Parseable):

    @staticmethod
    def parse(obj, raw=False):
        if raw:
            return obj.s
        return "'{}'".format(obj.s)
