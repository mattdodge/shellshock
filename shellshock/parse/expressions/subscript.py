from shellshock.parse import Parseable, parse


class SubscriptType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
