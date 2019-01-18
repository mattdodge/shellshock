from shellshock.parse import Parseable, parse, Unparseable


class CompareType(Parseable):

    @staticmethod
    def parse(obj):
        if len(obj.ops) != 1:
            raise Unparseable("Compare operations must one and only have one operation")
        if len(obj.comparators) != 1:
            raise Unparseable("Compare operations must one and only have one comparator")
        return "{} {} {}".format(
            parse(obj.left),
            parse(obj.ops[0]),
            parse(obj.comparators[0]),
        )
