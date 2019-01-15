from shellshock.parse import Parseable, parse


class AndType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
