from shellshock.converters import converter
from shellshock.parse import parse


def _file_check(test, call_args):
    return "{} {}".format(test, parse(call_args[0]))


@converter('ss.file_exists')
def file_exists(call_args, **kwargs):
    return _file_check('-e', call_args)


@converter('ss.file_is_file')
def file_is_file(call_args, **kwargs):
    return _file_check('-f', call_args)


@converter('ss.file_has_contents')
def file_has_contents(call_args, **kwargs):
    return _file_check('-s', call_args)


@converter('ss.file_is_dir')
def file_is_dir(call_args, **kwargs):
    return _file_check('-d', call_args)


@converter('ss.file_is_block')
def file_is_block(call_args, **kwargs):
    return _file_check('-b', call_args)


@converter('ss.file_is_character')
def file_is_character(call_args, **kwargs):
    return _file_check('-c', call_args)


@converter('ss.file_is_pipe')
def file_is_pipe(call_args, **kwargs):
    return _file_check('-p', call_args)


@converter('ss.file_is_symlink')
def file_is_symlink(call_args, **kwargs):
    return _file_check('-L', call_args)


@converter('ss.file_is_terminal')
def file_is_terminal(call_args, **kwargs):
    return _file_check('-t', call_args)


@converter('ss.file_has_read')
def file_has_read(call_args, **kwargs):
    return _file_check('-r', call_args)


@converter('ss.file_has_write')
def file_has_write(call_args, **kwargs):
    return _file_check('-w', call_args)


@converter('ss.file_has_execute')
def file_has_execute(call_args, **kwargs):
    return _file_check('-x', call_args)
