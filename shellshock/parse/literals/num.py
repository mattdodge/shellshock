from shellshock.parse import Parseable, parse


class NumType(Parseable):

    @staticmethod
    def parse(obj):
        return "{}".format(obj.n)
