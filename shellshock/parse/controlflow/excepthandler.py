from shellshock.parse import Parseable, parse


class ExceptHandlerType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
