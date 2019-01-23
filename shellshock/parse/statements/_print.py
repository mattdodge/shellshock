from shellshock.parse import Parseable, parse


class PrintType(Parseable):

    @staticmethod
    def parse(obj):
        return "echo {}".format(
            " ".join([parse(value) for value in obj.values]))
