from shellshock.parse import Parseable, parse


class LShiftType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
