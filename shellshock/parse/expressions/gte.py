from shellshock.parse import Parseable, Unparseable


class GtEType(Parseable):

    @staticmethod
    def parse(obj, numeric=False):
        if numeric:
            return '-ge'
        raise Unparseable("No greater equal support on strings")
