from ast import Num
from .parse import parse


class Parseable():

    _known_vars = set()
    _known_funcs = set()
    _known_refs = {
        "print",
    }
    _known_mocks = {}

    @staticmethod
    def parse(obj):
        raise NotImplementedError

    @classmethod
    def reset(cls):
        cls._known_vars = set()

    @classmethod
    def is_numeric(cls, obj):
        """ Returns true if an object appears to be a number """
        if isinstance(obj, Num):
            return True

        try:
            float(parse(obj))
            return True
        except ValueError:
            return False
