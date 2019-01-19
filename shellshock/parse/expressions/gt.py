from shellshock.parse import Parseable


class GtType(Parseable):

    @staticmethod
    def parse(obj, numeric=False):
        if numeric:
            return '-gt'
        return "\\>"
