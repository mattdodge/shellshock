

def shell(call_ref):
    from shellshock.parse import parse
    arg = call_ref.args[0]
    return parse(arg, raw=True).strip()
