from shellshock.parse import Parseable, Unparseable


class ImportType(Parseable):

    @staticmethod
    def parse(obj):
        if obj.names[0].name == "shellshock":
            pass
        else:
            raise Unparseable("Only imports of shellshock are allowed")
