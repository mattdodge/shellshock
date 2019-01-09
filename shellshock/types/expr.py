from .base import TypeInterface
from ast import Expr


class ExprType(TypeInterface):

    type_to_match = Expr

    @classmethod
    def convert(cls, node):
        return cls.convert_node(node.value)
