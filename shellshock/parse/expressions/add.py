from shellshock.parse import Parseable, parse


class AddType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
