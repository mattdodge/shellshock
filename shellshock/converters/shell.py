from shellshock.converters import converter
from shellshock.convert import ConvertContext
from shellshock.parse import parse


@converter('ss.shell')
def shell(args, kwargs):
    arg = args[0]
    return parse(arg, raw=True).strip()


@converter('ss.shebang')
def shebang(args, kwargs):
    ConvertContext.shebang = parse(args[0], raw=True)


@converter('ss.exit')
def exit(args, kwargs):
    return "exit {}".format(parse(args[0]))


@converter('print')
def print(args):
    return "echo -e {}".format(" ".join([parse(arg) for arg in args]))
