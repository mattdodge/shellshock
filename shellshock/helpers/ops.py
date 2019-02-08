from shellshock.helpers import helper
from shellshock.parse import parse


@helper('ss.noop')
def noop(args, kwargs):
    return ":"
