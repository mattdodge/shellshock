from . import parse, Unparseable


def parse_body(ast_body):
    from shellshock.convert import ConvertContext
    parsed_lines = []
    ConvertContext.indent_level += 1
    for node in ast_body:
        if ConvertContext.include_source:
            parsed_lines.extend([
                "# Original source",
                "# " + ConvertContext.get_line(node),
            ])

        try:
            node_out = parse(node)
        except NotImplementedError:
            if ConvertContext.allow_errors:
                node_out = "# Operation not allowed on line : {}".format(
                    ConvertContext.get_line(node))
            else:
                raise

        except Unparseable as e:
            if ConvertContext.allow_errors:
                node_out = "# Unknown parse of source code {}".format(e)
            else:
                raise

        if node_out:
            # Allow our parse method to return a list of lines instead of 1
            if isinstance(node_out, list):
                parsed_lines.extend(node_out)
            else:
                parsed_lines.append(node_out)

    ConvertContext.indent_level -= 1
    out_lines = []
    for parsed_line in parsed_lines:
        if parsed_line.startswith(" "):
            # If it starts with a space then it means it's already gone
            # through the parse_body indentation
            out_lines.append(parsed_line)
        else:
            out_lines.append("  " * ConvertContext.indent_level + parsed_line)
    return "\n".join(out_lines)
