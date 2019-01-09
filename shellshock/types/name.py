from ast import Name
from .base import TypeInterface


class NameType(TypeInterface):

    type_to_match = Name

    @classmethod
    def convert(cls, node):
        return "${}".format(node.id)
