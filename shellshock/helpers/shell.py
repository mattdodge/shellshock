from shellshock.helpers import helper
from shellshock.parse import parse


@helper('ss.shell')
def shell(args, kwargs):
    arg = args[0]
    return parse(arg, raw=True).strip()


@helper('print')
def print(args):
    return "echo {}".format(" ".join([parse(arg) for arg in args]))
