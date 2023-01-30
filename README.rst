sphinxcontrib-codeblock-callouts
=================================

``sphinxcontrib-codeblock-callouts`` is a Sphinx extension to mark "callouts" for
code-blocks up::

  def hello():  # 1
      return 'world'  # 2

Usage
-----

Append this extension in conf.py::

    extensions = ['sphinxcontrib.codeblock.callouts']

And build your document. That's all.

.. note:: This extension supports HTML builders only.


Syntax
------

Write callout numbers as comments into your source code::

    .. code-block:: python

       def hello():  # 1
           return 'world'  # 2

Addition to this, you can write callout texts via `code-block-callouts` directive::

    .. code-block-callouts::

       1. Definition of the "hello" function
       2. It will return a string "world" as a return value
