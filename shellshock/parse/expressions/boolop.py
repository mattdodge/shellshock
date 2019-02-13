from shellshock.parse import Parseable, parse


class BoolOpType(Parseable):

    @staticmethod
    def parse(obj):
        """ Bool operations in non-if statements

        The _if.py parser handles a boolean operation in an if statement
          e.g., if var1 and var2:
        So if we're here it means we're in some other expression
          e.g., chmod +x file || echo "No file found"
        """
        return " {} ".format(parse(obj.op)).join(
            [parse(val) for val in obj.values])
