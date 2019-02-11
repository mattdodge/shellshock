from shellshock.converters import converter
from shellshock.parse import parse


@converter('ss.noop')
def noop(call_args, **kwargs):
    return ":"
