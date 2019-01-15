from shellshock.parse import Parseable, parse


class StoreType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
