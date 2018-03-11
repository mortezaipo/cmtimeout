CMTimeOut
=========
Python ContextManager timeout handler library.


Install
=======

.. code-block:: shell

    $ pip install cmtimeout


Examples
========

Example 1:

.. code-block:: python

    from cmtimeout import CMTimeOut

    with CMTimeOut(2):
        with open("interface.fifo", "w") as f:
            pass


Example 2:

.. code-block:: python

    from cmtimeout import CMTimeOut, CMTimeOutException

    try:
        with CMTimeOut(2, True):
            with open("interface.fifo", "w") as f:
                pass
    except CMTimeOutException:
        print("opening file failed.")


Contribute
==========
Kindly keep me posted in case of any issue or question by opening new file is issue_ page or send me a pull request.

.. _issue: https://github.com/mortezaipo/cmtimeout/issues

