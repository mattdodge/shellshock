from shellshock.converters import converter
from shellshock.parse import parse


_colors_used = False


def _color(color_code, args):
    from shellshock.convert import ConvertContext
    ConvertContext.colors_used = True
    return ("${{SHELLSHOCK_COLOR_{color_code}}}"
            "{text}"
            "${{SHELLSHOCK_COLOR_EC}}".format(
                color_code=color_code,
                text=parse(args[0], raw=True),
            ))


@converter('ss.red')
def red(args, kwargs):
    return _color('RC', args)


@converter('ss.green')
def green(args, kwargs):
    return _color('GC', args)


@converter('ss.blue')
def blue(args, kwargs):
    return _color('BC', args)


@converter('ss.yellow')
def yellow(args, kwargs):
    return _color('YC', args)


@converter('ss.cyan')
def cyan(args, kwargs):
    return _color('CC', args)


def _get_color_init():
    """ Return the color checker script for the beginning of the file """
    return """
_SS_COLORS=$(tput colors 2>/dev/null || echo 0)
__detect_color_support() {
    if [ $? -eq 0 ] && [ "$_SS_COLORS" -gt 2 ]; then
        SHELLSHOCK_COLOR_RC='\\033[1;31m'
        SHELLSHOCK_COLOR_GC='\\033[1;32m'
        SHELLSHOCK_COLOR_BC='\\033[1;34m'
        SHELLSHOCK_COLOR_YC='\\033[1;33m'
        SHELLSHOCK_COLOR_CC='\\033[1;36m'
        SHELLSHOCK_COLOR_EC='\\033[0m'
        echo matt
    else
        SHELLSHOCK_COLOR_RC=""
        SHELLSHOCK_COLOR_GC=""
        SHELLSHOCK_COLOR_BC=""
        SHELLSHOCK_COLOR_YC=""
        SHELLSHOCK_COLOR_CC=""
        SHELLSHOCK_COLOR_EC=""
    fi
}
__detect_color_support
"""
