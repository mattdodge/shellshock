from shellshock.parse import Parseable


class NameType(Parseable):

    @staticmethod
    def parse(obj):
        return "${}".format(obj.id)
