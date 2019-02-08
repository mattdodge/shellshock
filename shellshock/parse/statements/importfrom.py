from shellshock.parse import Parseable


class ImportFromType(Parseable):

    @staticmethod
    def parse(obj):
        # Imports are allowed but ignored
        pass
