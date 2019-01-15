from shellshock.parse import Parseable, parse


class LoadType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
