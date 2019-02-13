from shellshock.parse import Parseable


class AddType(Parseable):

    @staticmethod
    def parse(obj):
        return "+"
