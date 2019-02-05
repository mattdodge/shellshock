from shellshock.parse import Parseable, parse
from shellshock.helpers import get_helper


class CallType(Parseable):

    @classmethod
    def parse(cls, obj):
        func_name = parse(obj.func)

        # Process keyword args to see if this is a func call ID to mock
        for kwarg in obj.keywords:
            if kwarg.arg == '__id__':
                mock_id = parse(kwarg.value, raw=True)
                if mock_id in cls._known_mocks:
                    # Record the mock call before processing the side effect
                    return [
                        '__record_mock_call {} {}'.format(
                            mock_id,
                            " ".join([parse(arg) for arg in obj.args]),
                        ),
                        '__mock_{}'.format(mock_id)
                    ]

        if func_name == 'print':
            return "echo {}".format(parse(obj.args[0]))
        elif func_name.startswith('ss.'):
            return get_helper(obj.func.attr, obj)
        else:
            return "{} {}".format(
                func_name,
                " ".join([parse(arg) for arg in obj.args]),
            )
