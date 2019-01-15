from shellshock.parse import Parseable, parse


class LambdaType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
