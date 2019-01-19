from ast import Num
from shellshock.parse import Parseable, parse, Unparseable


class CompareType(Parseable):

    @staticmethod
    def parse(obj):
        if len(obj.ops) != 1:
            raise Unparseable(
                "Compare operations must one and only have one operation")
        if len(obj.comparators) != 1:
            raise Unparseable(
                "Compare operations must one and only have one comparator")
        numeric_compare = False
        if isinstance(obj.left, Num) or isinstance(obj.comparators[0], Num):
            numeric_compare = True
        return "{} {} {}".format(
            parse(obj.left),
            parse(obj.ops[0], numeric=numeric_compare),
            parse(obj.comparators[0]),
        )
