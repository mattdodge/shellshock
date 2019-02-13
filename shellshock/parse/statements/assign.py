from ast import Call
from hashlib import sha256
from random import randint
from shellshock.parse import Parseable, parse


class AssignType(Parseable):

    @classmethod
    def parse(cls, obj):
        assign_target = obj.targets[0].id
        cls._known_vars.add(assign_target)
        if isinstance(obj.value, Call) and obj.value.func.attr == 'input':
            # If we're assigning from user input, adjust accordingly
            return cls._read_input_into_var(assign_target, obj)
        else:
            return "{}={}".format(
                assign_target,
                parse(obj.value),
            )

    @classmethod
    def _read_input_into_var(cls, var, obj):
        """ Read user input into variable

        At this point we assume obj.value is a Call object pointing to
        ss.input and obj.value.args[0] is the input prompt. We know the user
        is trying to set this input to a new variable, but we must make a temp
        variable in between. The variable name will be based off the hash of
        the prompt for repeatability's sake.
        """
        prompt_hash = sha256()
        prompt_hash.update(obj.value.args[0].s.encode())
        temp_var = "INPUT_VAR_{}".format(prompt_hash.hexdigest()[:8])
        return [
            parse(obj.value, assign_to_var=temp_var),
            "{new_var}=\"${temp_var}\"".format(new_var=var, temp_var=temp_var),
        ]
