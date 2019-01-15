from shellshock.parse import Parseable, parse


class NameConstantType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
