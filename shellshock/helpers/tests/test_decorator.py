from unittest import TestCase
from unittest.mock import Mock
from shellshock.helpers import helper, run_helper


@helper('myfunc_args')
def helper_args(args):
    return "only args"


@helper('myfunc_kwargs')
def helper_args_kwargs(args, kwargs):
    return "with kwargs"


class TestHelperDecorator(TestCase):

    def test_args(self):
        """ Test a function can take only args """
        mock_call = Mock()
        self.assertEqual(run_helper('myfunc_args', mock_call), "only args")

    def test_args_kwargs(self):
        """ Test a function can take optional kwargs too"""
        mock_call = Mock()
        self.assertEqual(run_helper('myfunc_kwargs', mock_call), "with kwargs")
