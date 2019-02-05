from shellshock.parse import Parseable, parse


class NameConstantType(Parseable):

    @staticmethod
    def parse(obj):
        if obj.value == True:
            return "true"
        elif obj.value == False:
            return "false"
        elif obj.value == None:
            return "none"
