from shellshock.parse import Parseable, parse


class ArgType(Parseable):

    @staticmethod
    def parse(obj, arg_num, arg_default):
        trailing = ""
        if arg_default:
            trailing = ":-{}".format(parse(arg_default))
        return "  {}=${{{}{}}}".format(obj.arg, arg_num, trailing)
