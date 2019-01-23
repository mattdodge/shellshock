import os
import setuptools
from setuptools.command.install import install
import sys

VERSION = '0.0.1'

with open("README.md", "r") as fh:
    long_description = fh.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            sys.exit(
                "Git tag: {0} does not match the version of "
                "this app: {1}".format(tag, VERSION))


setuptools.setup(
    name="shellshock",
    version=VERSION,
    author="Matt Dodge",
    author_email="mattedgod@gmail.com",
    description="Write your shell scripts using Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mattdodge/shellshock",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'shellshock=shellshock.main:main',
        ],
    },
    cmdclass={
        'verify': VerifyVersionCommand,
    },
)
