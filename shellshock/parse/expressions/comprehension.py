from shellshock.parse import Parseable, parse


class ComprehensionType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
