from shellshock.parse import Parseable, parse


class CallType(Parseable):

    @staticmethod
    def parse(obj):
        func_name = obj.func.id

        if func_name == 'print':
            return "echo {}".format(parse(obj.args[0]))
        return "{} {}".format(func_name, obj.args)
