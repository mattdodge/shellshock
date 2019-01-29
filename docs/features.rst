Python feature compatability
============================

.. list-table::
   :widths: 15 10 20
   :header-rows: 1

   * - Python Feature
     - Shellshock Support
     - Example
   * - Strings
     - YES
     - .. code-block:: python

           "here we go"

   * - Integers/Floats
     - YES
     - .. code-block:: python

           my_val = 3.14

   * - Function definitions
     - YES
     - .. code-block:: python

           def doit(var1, var2='default'):
               print(var1)
               print(var2)
           doit('once', 'twice')
