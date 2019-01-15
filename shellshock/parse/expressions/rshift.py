from shellshock.parse import Parseable, parse


class RShiftType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
