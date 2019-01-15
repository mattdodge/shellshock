from shellshock.parse import Parseable, parse


class DictCompType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
