Converter Reference
===================

Shellshock comes with many useful converter functions built-in. Here is the reference of these functions.

Examples are provided for most functions. For examples assume `script.py` is the input Shellshock script and `script.sh` is the output after Shellshock transpilation.

.. function:: shell(raw_shell_cmd)
    :module: ss

    Run a raw shell command. The argument will be output in its entirety.

    Use this method when you want to write regular shell commands in your script.

    **Example: Basic Usage**

    .. code-block:: python
        :caption: script.py

        import shellshock as ss
        ss.shell("chown 755 myfile")


    .. code-block:: sh
        :caption: script.sh

        #!/bin/sh
        chown 755 myfile

    | **Example: Convert Existing Script**
    | Wrap an entire existing shell script (or a part of a script) in `ss.shell` to partially migrate an existing script to Shellshock

    .. code-block:: python
        :caption: script.py

        import shellshock as ss
        ss.shell("""
        chown 755 myfile
        # other existing shell script
        echo "output"
        """)


    .. code-block:: sh
        :caption: script.sh

        #!/bin/sh
        chown 755 myfile
        # other existing shell script
        echo "output"
