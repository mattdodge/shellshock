from shellshock.parse import Parseable, parse


class JoinedStrType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
