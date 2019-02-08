from shellshock.parse import Parseable


class ImportType(Parseable):

    @staticmethod
    def parse(obj):
        # Imports are allowed but ignored
        pass
