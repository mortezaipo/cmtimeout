IOTimeOut
=========
IO timeout handler library for Python.


Install
=======

.. code-block:: shell

    $ pip install iotimeout


Examples
========

Example 1:

.. code-block:: python

    from iotimeout import IOTimeOut

    with IOTimeOut(2):
        with open("interface.fifo", "w") as f:
            pass


Example 2:

.. code-block:: python

    from iotimeout import IOTimeOut, IOTimeOutException

    try:
        with IOTimeOut(2, True):
            with open("interface.fifo", "w") as f:
                pass
    except IOTimeOutException:
        print("opening file failed.")


Contribute
==========
Kindly keep me posted in case of any issue or question by opening new file is issue_ page or send me a pull request.

.. _issue: https://github.com/mortezaipo/iotimeout/issues

