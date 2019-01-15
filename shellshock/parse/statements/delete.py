from shellshock.parse import Parseable, parse


class DeleteType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
