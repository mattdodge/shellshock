from shellshock.parse import Parseable, parse


class ArgumentsType(Parseable):

    @classmethod
    def parse(cls, obj):
        arg_list = []
        num_args = len(obj.args)
        num_defaults = len(obj.defaults)
        for arg_index, arg in enumerate(obj.args):
            cls._known_vars.add(arg.arg)
            default = None
            default_index = arg_index + num_defaults - num_args
            if default_index >= 0:
                default = obj.defaults[default_index]
            arg_list.append(parse(
                arg,
                arg_num=(arg_index + 1),
                arg_default=default,
            ))
        return "\n".join(arg_list)
