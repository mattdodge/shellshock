from shellshock.parse import parse

known_converters = {}


def run_converter(func, call_ref, parseable, context, **kwargs):
    from shellshock.parse import Unparseable
    if func in known_converters:
        try:
            return known_converters[func](
                call_ref.args,
                call_ref.keywords,
                parseable=parseable,
                context=context,
                **kwargs,
            )
        except TypeError:
            return known_converters[func](
                call_ref.args,
                parseable=parseable,
                context=context,
                **kwargs,
            )
    raise Unparseable("Unknown converter function {}".format(func))


def converter(function_name):
    def wrapped_func(func):
        known_converters[function_name] = func
        return func
    return wrapped_func


__get_kwarg_default = -1


def get_kwarg(call_kwargs, kwarg_name, default=__get_kwarg_default, **kwargs):
    """ Return the value of a kwarg in a converter call """
    for kwarg in call_kwargs:
        if kwarg.arg == kwarg_name:
            default = parse(kwarg.value, **kwargs)
            break
    if default is __get_kwarg_default:
        raise KeyError("Required kwarg '{}' was not provided".format(kwarg_name))
    return default
