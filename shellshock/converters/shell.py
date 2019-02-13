from shellshock.converters import converter
from shellshock.parse import parse


@converter('ss.shell')
def shell(call_args, **kwargs):
    arg = call_args[0]
    return parse(arg, raw=True).strip()


@converter('ss.subshell')
def subshell(call_args, **kwargs):
    """ Run the argument in a subshell, return the result """
    return "$({})".format(parse(call_args[0], raw=True))


@converter('ss.shebang')
def shebang(call_args, context=None, **kwargs):
    context.shebang = parse(call_args[0], raw=True)


@converter('sys.exit')
@converter('ss.exit')
def exit(call_args, **kwargs):
    return "exit {}".format(parse(call_args[0]))


@converter('print')
def print(call_args, **kwargs):
    return "echo -e {}".format(" ".join([parse(arg) for arg in call_args]))


@converter('ss.envvar')
def envvar(call_args, call_kwargs, parseable=None, **kwargs):
    default = None
    for call_kwarg in call_kwargs:
        if call_kwarg.arg == 'default':
            default = parse(call_kwarg.value)
    var_name = parse(call_args[0], raw=True)
    parseable._known_vars.add(var_name)
    if default is not None:
        return "{var}=${{{var}:-{default}}}".format(
            var=var_name,
            default=default)
