from unittest import TestCase
from unittest.mock import Mock, patch
from shellshock.converters import converter, run_converter, get_kwarg


@converter('myfunc_args')
def converter_args(call_args, *args, **kwargs):
    return "only args"


@converter('myfunc_kwargs')
def converter_args_kwargs(call_args, call_kwargs, *args, **kwargs):
    return "with kwargs"


class TestConverter(TestCase):

    def test_decorator_args(self):
        """ Test a function can take only args """
        mock_call = Mock()
        self.assertEqual(
            run_converter(
                'myfunc_args', mock_call, parseable=self, context=None),
            "only args")

    def test_decorator_args_kwargs(self):
        """ Test a function can take optional kwargs too"""
        mock_call = Mock()
        self.assertEqual(
            run_converter(
                'myfunc_kwargs', mock_call, parseable=self, context=None),
            "with kwargs")

    def test_get_kwarg(self):
        """ Make sure we can get a kwarg from a call args list """
        mock_kwarg_1 = Mock()
        mock_kwarg_1.arg = 'arg1'
        mock_kwarg_1.value = 'value1'
        mock_kwarg_2 = Mock()
        mock_kwarg_2.arg = 'arg2'
        mock_kwarg_2.value = 'value2'
        # Grab arg2 and it works
        with patch('shellshock.converters.parse', side_effect=lambda x: x):
            result = get_kwarg([mock_kwarg_1, mock_kwarg_2], 'arg2')
        self.assertEqual(result, 'value2')

        # Grab arg3 (nonexistent) and it works
        with patch('shellshock.converters.parse', side_effect=lambda x: x):
            result = get_kwarg([mock_kwarg_1, mock_kwarg_2], 'arg2')
        self.assertEqual(result, 'value2')

    def test_get_kwarg_default(self):
        """ Make sure we can get a default kwarg if it's not set """
        mock_kwarg_1 = Mock()
        mock_kwarg_1.arg = 'arg1'
        mock_kwarg_1.value = 'value1'
        # Grab arg2 and it works
        with patch('shellshock.converters.parse', side_effect=lambda x: x):
            result = get_kwarg([mock_kwarg_1], 'notreal', default='test')
        self.assertEqual(result, 'test')

    def test_get_kwarg_no_default(self):
        """ Make sure if no default is provided we get an exception """
        mock_kwarg_1 = Mock()
        mock_kwarg_1.arg = 'arg1'
        mock_kwarg_1.value = 'value1'
        # Grab arg2 and it works
        with patch('shellshock.converters.parse', side_effect=lambda x: x):
            result = get_kwarg([mock_kwarg_1], 'notreal', default='test')
        self.assertEqual(result, 'test')

    def test_get_kwarg_missing_default(self):
        """ Make sure we can get a default kwarg if it's not set """
        mock_kwarg_1 = Mock()
        mock_kwarg_1.arg = 'arg1'
        mock_kwarg_1.value = 'value1'
        # Grab arg2 and it works
        with patch('shellshock.converters.parse', side_effect=lambda x: x):
            with self.assertRaises(KeyError):
                get_kwarg([mock_kwarg_1], 'notreal')
