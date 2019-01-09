from ..exceptions import Unparseable
from . import get_types


class TypeInterface():

    # The class type this converter matches
    type_to_match = None

    @classmethod
    def convert(cls, node):
        raise NotImplemented

    @classmethod
    def convert_node(cls, node):
        """ Take a generic node and find the best converter """
        for _type in get_types():
            if isinstance(node, _type.type_to_match):
                return _type.convert(node)
        raise Unparseable
