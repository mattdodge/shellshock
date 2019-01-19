from shellshock.parse import Unparseable, Parseable


class LtEType(Parseable):

    @staticmethod
    def parse(obj, numeric=False):
        if numeric:
            return '-le'
        raise Unparseable("No less equal support on strings")
