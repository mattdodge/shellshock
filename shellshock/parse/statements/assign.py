from shellshock.parse import Parseable, parse


class AssignType(Parseable):

    @staticmethod
    def parse(obj):
        return "{}={}".format(
            obj.targets[0].id,
            parse(obj.value),
        )
