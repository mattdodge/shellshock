from shellshock.parse import Parseable, parse


class LtType(Parseable):

    @staticmethod
    def parse(obj, numeric=False):
        if numeric:
            return '-lt'
        return "\\<"
