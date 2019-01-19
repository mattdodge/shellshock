from shellshock.parse import Parseable, parse


class NotEqType(Parseable):

    @staticmethod
    def parse(obj, numeric=False):
        if numeric:
            return '-ne'
        return "!="
