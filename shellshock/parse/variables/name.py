from shellshock.parse import Parseable, parse


class NameType(Parseable):

    @staticmethod
    def parse(obj):
        return "${}".format(obj.id)
