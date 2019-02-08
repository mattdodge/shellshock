
known_helpers = {}


def run_helper(func, call_ref):
    from shellshock.parse import Unparseable
    if func in known_helpers:
        try:
            return known_helpers[func](call_ref.args, call_ref.keywords)
        except TypeError:
            return known_helpers[func](call_ref.args)
    raise Unparseable("Unknown helper function {}".format(func))


def helper(function_name):
    def wrapped_func(func):
        known_helpers[function_name] = func
        return func
    return wrapped_func
