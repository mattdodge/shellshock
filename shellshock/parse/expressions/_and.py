from shellshock.parse import Parseable


class AndType(Parseable):

    @staticmethod
    def parse(obj):
        return "&&"
