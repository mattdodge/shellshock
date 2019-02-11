import ast
from unittest import TestCase
from shellshock.parse import Parseable, Unparseable
from shellshock.convert import ConvertContext, load_converters
from shellshock.parse.body import parse_body


class ParseTestCase(TestCase):

    def setUp(self):
        super(ParseTestCase, self).setUp()
        Parseable.reset()
        ConvertContext.reset()
        load_converters()

    def assert_parsed(self, source, output):
        parsed = parse_body(ast.parse(source).body)
        self.assertEqual(parsed, output.strip())

    def assert_parsed_raises(self, source, exc=Unparseable):
        with self.assertRaises(exc):
            parse_body(ast.parse(source).body)
