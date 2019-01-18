from shellshock.parse import Parseable, parse
from shellshock.helpers import get_helper


class CallType(Parseable):

    @staticmethod
    def parse(obj):
        func_name = parse(obj.func)

        if func_name == 'print':
            return "echo {}".format(parse(obj.args[0]))
        elif func_name.startswith('ss.'):
            return get_helper(obj.func.attr, obj)
        return "{} {}".format(func_name, obj.args)
