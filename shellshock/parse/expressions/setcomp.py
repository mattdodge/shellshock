from shellshock.parse import Parseable, parse


class SetCompType(Parseable):

    @staticmethod
    def parse(obj):
        raise NotImplementedError
