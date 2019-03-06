import shellshock as ss


def does_something(var):
    print(var)
    var = 10
    print(var)


does_something(3, __id__='funccall')

if not ss.file_has_execute(ss.subshell('command -v myfakecommand'), __id__='command_exists'):
    print("Command doesnt exist")
else:
    print("Command exists")
