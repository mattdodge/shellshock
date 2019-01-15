from shellshock.parse import Parseable


class NumType(Parseable):

    @staticmethod
    def parse(obj):
        return "{}".format(obj.n)
