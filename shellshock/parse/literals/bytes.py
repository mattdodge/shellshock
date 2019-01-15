from shellshock.parse import Parseable, parse


class BytesType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
