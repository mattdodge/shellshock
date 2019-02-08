from shellshock.parse import Parseable


class ImportFromType(Parseable):

    @classmethod
    def parse(cls, obj):
        # Imports just declare our reference
        for names in obj.names:
            cls._known_refs.add(names.name)
