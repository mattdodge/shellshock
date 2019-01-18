from shellshock.parse import Unparseable


def get_helper(func, call_ref):
    import shellshock.helpers.shell as shell
    if func == "shell":
        return shell.shell(call_ref)
    else:
        raise Unparseable("Unknown helper function {}".format(func))
