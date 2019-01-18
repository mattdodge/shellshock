from shellshock.parse import Parseable, parse


class AttributeType(Parseable):

    @staticmethod
    def parse(obj):
        """ Returns a stringified version of the attr. """
        return "{}.{}".format(
            parse(obj.value),
            obj.attr)
