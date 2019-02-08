
known_converters = {}


def run_converter(func, call_ref):
    from shellshock.parse import Unparseable
    if func in known_converters:
        try:
            return known_converters[func](call_ref.args, call_ref.keywords)
        except TypeError:
            return known_converters[func](call_ref.args)
    raise Unparseable("Unknown converter function {}".format(func))


def converter(function_name):
    def wrapped_func(func):
        known_converters[function_name] = func
        return func
    return wrapped_func
