
.. Jacob's blog post example, created by `ablog start` on Oct 06, 2022.

.. post:: Oct 01, 2022
   :tags: githubpage, sphinx, tutorial
   :category: Chores
   :author: TIAN Zeyu


###########################
GithubPage Sphinx Tutorial
###########################

first few steps
================


.. code-block:: shell

    # create folder
    mkdir username.github.io
    # create new file for poetry
    touch pyproject.toml

    # poetry add related dependencies
    poetry add ablog
    poetry add sphinx-rtd-theme
    poetry add sphinxcontrib-napoleon
    poetry add myst-parser
    poetry add sphinx-autobuild
    poetry add sphinx-autodoc-typehints

    # ablog
    ablog start
    ablog build
    # note that ablog deploy function is not used for this project as the use-case for the deploy function is very strict, and the author didn't get it working. So the deployment is done manually by adding .nojekyll and index.html file.

    # at root folder, create new files/folders for github page
    touch .nojekyll
    touch index.html
    echo "<meta http-equiv=\"refresh\" content=\"0; url=./_website/index.html\" />" > index.html
    mkdir blog
    mkdir blog/2022-10/...

    # initialise your git
    git init
    touch .gitignore

    # how to render locally
    sphinx-autobuild . ./_website


pyproject.toml
===============

a sample project toml file example:


.. code-block:: shell

    [tool.poetry]
    name = "zeyutiann.github.io"
    version = "0.1.0"
    description = ""
    authors = ["Zeyu Tian <olivandertian@yahoo.com>"]
    readme = "./blog/2022-10/2022-10-01-githubpage-tutorial.rst"
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


index.html
============

a sample for index.html


.. code-block:: html

    <meta http-equiv="refresh" content="0; url=./_website/index.html" />


tags and category
==================

common tags and category are documented here:
    - tags can be anything, it's the one word summary for the blog.
    - categories are restricted as below.

* tags
    * sphinx
    * poetry

* category
    * Python
    * Git
    * Java
    * Cpp
    * Kx
    * DesignPattern
    * Algorithm
    * Chores



reference:
===========

- https://documentation-style-guide-sphinx.readthedocs.io/en/latest/
-



