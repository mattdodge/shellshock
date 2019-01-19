from shellshock.parse import Parseable


class EqType(Parseable):

    @staticmethod
    def parse(obj, numeric=False):
        if numeric:
            return '-eq'
        return "=="
