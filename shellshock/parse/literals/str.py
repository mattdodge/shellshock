from shellshock.parse import Parseable


class StrType(Parseable):

    @classmethod
    def parse(cls, obj, raw=False):
        if raw:
            return obj.s
        return "'{}'".format(cls._escape_single_quotes(obj.s))

    @staticmethod
    def _escape_single_quotes(s):
        """ Allow single quotes in strings

        This replaces single quotes with the following sequence:
         - closing single quote
         - escaped single quote
         - re-opening single quote
       """
        return s.replace("'", "'\\''")
