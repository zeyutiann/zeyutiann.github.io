
.. Jacob's blog post example, created by `ablog start` on Oct 06, 2022.

.. post:: Oct 06, 2022
   :tags: githubpage-sphinx-tutorial
   :category: Chore
   :author: TIAN Zeyu


################
How to
################

.. code-block:: shell

    touch pyproject.toml
    poetry add ablog
    poetry add sphinx-rtd-theme
    poetry add sphinxcontrib-napoleon
    poetry add myst-parser

    touch .nojekyll
    git


a sample project toml file:

.. code-block:: shell

    [tool.poetry]
    name = "zeyutiann.github.io"
    version = "0.1.0"
    description = ""
    authors = ["Zeyu Tian <olivandertian@yahoo.com>"]
    readme = "README.rst"
    packages = [{include = "poetry_demo"}]

    [tool.poetry.dependencies]
    python = "^3.7"
    ablog = "^0.10.29"
    sphinx-rtd-theme = "^1.0.0"
    sphinxcontrib-napoleon = "^0.7"
    myst-parser = "^0.18.1"


    [build-system]
    requires = ["poetry-core"]
    build-backend = "poetry.core.masonry.api"


