.. post:: 2022.09.29
   :tags: sphinx
   :category: Documentation
   :author: TIAN Zeyu




Sphinx and it's related tutorial
#################################

.. code-block::

    poetry sphinx-quickstart docs
    poetry run sphinx-build -b html docs/source/ docs/build/html


    cd docs
    poetry run make html

    poetry add sphinx-rtd-theme --group docs
    poetry add sphinx-autodoc-typehints --group docs
    poetry add sphinx-autobuild --group docs
    poetry add sphinxcontrib-napoleon --group docs

    poetry run sphinx-autobuild docs docs/build/html

how to document a class
========================
autodoc

autodoc reference
https://stackoverflow.com/questions/7753805/sphinx-automodule-how-to-reference-classes-in-same-module

Jupyter Notebook
=================
Because all code cells in a document are run in the same kernel, cells later in the document can use variables and functions defined in cells earlier in the document

.. jupyter-execute::

  name = 'world'
  print('hello ' + name + '!')

- https://jupyter-sphinx.readthedocs.io/en/latest/

how to inline code
===================

* create a document configuration file ``docutils.conf`` in the same directory as the sphinx configuration
* add to the docutils configuration file ``docutils.conf``:

    .. code-block:: shell

        [restructuredtext parser]
        syntax_highlight=short

    .. note::

        This option makes Pygments use short class names for the highlighted code. This lets you re-use the same Pygments style sheet pygments.css that Sphinx already uses for code blocks.

* for each language you want to highlight, create a custom interpreted text role using docutils' ``role`` directive

    .. code-block:: shell

        ..role:: python(code)
          :language: python
          :class: highlight

* use the new role to highlight inline code.

    .. code-block:: shell

        :python:`print("Hello World")

    This renders :python:`print("Hello World")`

How to include a python file
=============================

    .. code-block:: rst

        .. include:: ../path/to/file/name
           :code: python


Reference
==========
- https://www.sphinx-doc.org/en/master/tutorial/first-steps.html
- https://sphinxawesome.xyz/demo/inline-code/




