from shellshock.converters import converter
from shellshock.parse import parse


@converter('ss.noop')
def noop(args, kwargs):
    return ":"
