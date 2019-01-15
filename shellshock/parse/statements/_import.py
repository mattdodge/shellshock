from shellshock.parse import Parseable, parse


class ImportType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
