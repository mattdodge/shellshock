from shellshock.parse import Parseable, parse


class FormattedValueType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
