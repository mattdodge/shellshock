from shellshock.parse import Parseable, Unparseable


class NameType(Parseable):

    @classmethod
    def parse(cls, obj):
        if obj.id in cls._known_vars:
            # Access to the variable needs a $
            return "${}".format(obj.id)
        elif obj.id in cls._known_refs:
            return obj.id
        else:
            raise Unparseable("Unknown name {}".format(obj.id))
