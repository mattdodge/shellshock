from ast import Str
from .base import TypeInterface


class StrType(TypeInterface):

    type_to_match = Str

    @classmethod
    def convert(cls, node):
        return "'{}'".format(node.s)
