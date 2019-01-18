from shellshock.parse import Parseable, parse


class IfType(Parseable):

    @staticmethod
    def parse(obj):
        return (
            "if [ {test} ]; then\n"
            "  {body}\n"
            "fi"
        ).format(
            test=parse(obj.test),
            body=parse(obj.body[0]),
        )
        raise NotImplementedError
