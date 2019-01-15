from shellshock.parse import Parseable, parse


class DictType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
