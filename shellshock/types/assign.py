from ast import Assign
from .base import TypeInterface


class AssignType(TypeInterface):

    type_to_match = Assign

    @classmethod
    def convert(cls, node):
        return "{}={}".format(
            node.targets[0].id,
            cls.convert_node(node.value),
        )
