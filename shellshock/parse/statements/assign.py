from shellshock.parse import Parseable, parse


class AssignType(Parseable):

    @classmethod
    def parse(cls, obj):
        assign_target = obj.targets[0].id
        cls._known_vars.add(assign_target)
        return "{}={}".format(
            assign_target,
            parse(obj.value),
        )
