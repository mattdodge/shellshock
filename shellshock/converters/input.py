from shellshock.converters import converter, get_kwarg
from shellshock.parse import parse


@converter('ss.input')
def input(
        call_args, call_kwargs, parseable=None, assign_to_var=None, **kwargs):
    if assign_to_var is not None:
        # See if we are assigning this to a new variable first
        target_var = assign_to_var
    else:
        # If we're not assigning, they better specify the 'target' kwarg
        target_var = get_kwarg(call_kwargs, 'target', raw=True)
    parseable._known_vars.add(target_var)

    return "read -p {prompt} {var} </dev/tty".format(
        prompt=parse(call_args[0]),
        var=target_var,
    )
