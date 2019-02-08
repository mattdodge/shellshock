from shellshock.converters import converter
from shellshock.parse import parse


@converter('customconverter')
def my_custom_converter(args):
    return "echo 'I came from a custom converter'  args -> {}".format(
        " ".join([parse(arg) for arg in args]))
