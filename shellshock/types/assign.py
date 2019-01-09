def convert(node):
    from ..parse import convert_node
    return "{}={}".format(
        node.targets[0].id,
        convert_node(node.value),
    )
