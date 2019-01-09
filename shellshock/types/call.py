def convert(node):
    from ..parse import convert_node
    func_name = node.func.id

    if func_name == 'print':
        return "echo {}".format(convert_node(node.args[0]))
    return "{} {}".format(func_name, node.args)
