from shellshock.parse import Parseable, parse


class ClassDefType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
