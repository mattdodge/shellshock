Getting Started
===============

A walkthrough highlighting the main features of Shellshock

Install
-------
If you haven't yet, install Shellshock

.. code-block:: shell

   pip install shellshock


Hello World
-----------
To start, we'll create the Hello World of Python/Shell scripts. Let's create a Python file called **script.py** that has the following contents:

.. code-block:: python

   print('Hello world!')

Now, you can convert this to a shell script using the Shellshock CLI. Without any arguments, Shellshock will output the resulting shell script to stdout.

.. code-block:: shell

   $ shellshock script.py
   echo 'Hello world!'

If you want, you can even pipe the output to your favorite shell to run it.

.. code-block:: shell

   $ shellshock script.py | bash
   Hello world!
