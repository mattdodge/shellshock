import subprocess


def shell(shell_cmd):
    subprocess.call(shell_cmd, shell=True)


def noop(*args, **kwargs):
    pass
