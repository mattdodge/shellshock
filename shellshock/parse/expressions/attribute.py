from shellshock.parse import Parseable, parse


class AttributeType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
