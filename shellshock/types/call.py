from ast import Call
from .base import TypeInterface


class CallType(TypeInterface):

    type_to_match = Call

    @classmethod
    def convert(cls, node):
        func_name = node.func.id

        if func_name == 'print':
            return "echo {}".format(cls.convert_node(node.args[0]))
        return "{} {}".format(func_name, node.args)
