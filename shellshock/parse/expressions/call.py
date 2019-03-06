from shellshock.parse import Parseable, parse
from shellshock.convert import ConvertContext
from shellshock.converters import run_converter


class CallType(Parseable):

    @classmethod
    def parse(cls, obj, **kwargs):
        func_name = parse(obj.func)

        # Process keyword args to see if this is a func call ID to mock
        for kwarg in obj.keywords:
            if kwarg.arg == '__id__':
                mock_id = parse(kwarg.value, raw=True)
                if mock_id in cls._known_mocks:
                    return cls._call_mock(mock_id, obj.args)

        if func_name in cls._known_funcs:
            return "{} {}".format(
                func_name,
                " ".join([parse(arg) for arg in obj.args]),
            )
        else:
            return run_converter(
                func=func_name,
                call_ref=obj,
                parseable=cls,
                context=ConvertContext,
                **kwargs,
            )

    @classmethod
    def _call_mock(cls, mock_id, mock_args):
        """ Call a unit test mock instead of the real method.

        This will spawn a subshell that does two things:
          1. Records the mock call with arguments for assertion in the test
          2. Calls a stub function that returns the mock side effect
        """
        return '$(__record_mock_call {mock} {args}; __mock_{mock})'.format(
            mock=mock_id,
            args=" ".join([parse(arg) for arg in mock_args]),
        )
