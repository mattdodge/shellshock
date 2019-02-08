from unittest import TestCase
from unittest.mock import Mock
from shellshock.converters import converter, run_converter


@converter('myfunc_args')
def converter_args(args):
    return "only args"


@converter('myfunc_kwargs')
def converter_args_kwargs(args, kwargs):
    return "with kwargs"


class TestConverterDecorator(TestCase):

    def test_args(self):
        """ Test a function can take only args """
        mock_call = Mock()
        self.assertEqual(run_converter('myfunc_args', mock_call), "only args")

    def test_args_kwargs(self):
        """ Test a function can take optional kwargs too"""
        mock_call = Mock()
        self.assertEqual(run_converter('myfunc_kwargs', mock_call), "with kwargs")
