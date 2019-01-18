import ast
from unittest import TestCase
from shellshock.parse import parse, Parseable, Unparseable


class ParseTestCase(TestCase):

    def setUp(self):
        super().setUp()
        Parseable.reset()

    def _parse_source(self, source):
        parsed = ast.parse(source)
        return parsed

    def assert_parsed(self, source, output):
        parsed = self._parse_source(source)
        actual_out_lines = []
        for node in parsed.body:
            actual_out_lines.append(parse(node))
        actual_out = "\n".join(actual_out_lines)
        self.assertEqual(actual_out, output.strip())

    def assert_parsed_raises(self, source, exc=Unparseable):
        parsed = self._parse_source(source)
        with self.assertRaises(exc):
            for node in parsed.body:
                parse(node)
