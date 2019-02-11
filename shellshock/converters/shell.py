from shellshock.converters import converter
from shellshock.convert import ConvertContext
from shellshock.parse import parse


@converter('ss.shell')
def shell(args, kwargs):
    arg = args[0]
    return parse(arg, raw=True).strip()


@converter('print')
def print(args):
    return "echo -e {}".format(" ".join([parse(arg) for arg in args]))
