from ast import Num
from .base import TypeInterface


class NumType(TypeInterface):

    type_to_match = Num

    @classmethod
    def convert(cls, node):
        return "{}".format(node.n)
