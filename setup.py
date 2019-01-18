import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shellshock",
    version="0.0.1",
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
)
