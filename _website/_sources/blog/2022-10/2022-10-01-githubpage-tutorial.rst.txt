
.. Jacob's blog post example, created by `ablog start` on Oct 06, 2022.

.. post:: 2022.10.01
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

markdown support
=================

Install myst-parser, and add these options to your conf.py

.. code-block:: python

    extensions=[...,
    "myst_parser",
    ...
    ]

    myst_update_mathjax = False

sample blog header format:

.. code-block:: shell

    ---
    blogpost: true
    date: Oct 10, 2020
    author: Nabil Freij
    location: World
    category: Manual
    language: English
    ---

Notice here we do not have a “:” at the start since the markdown metadata format is different from rst.

Please be aware that adding “myst-parser” will mean it will read all markdown files and try to parse them. You will need to use the following in your conf.py to prevent this:

.. code-block:: python

    exclude_patterns = [
        "posts/*/.ipynb_checkpoints/*",
        ".github/*",
        ".history",
        "github_submodule/*",
        "LICENSE.md",
        "README.md",
    ]

If you want to use Markdown files with extensions other than .md, adjust the source_suffix variable. The following example configures Sphinx to parse all files with the extensions .md and .txt as Markdown:

.. code-block:: python

    source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
    }

reference:
===========

- https://documentation-style-guide-sphinx.readthedocs.io/en/latest/
- https://ablog.readthedocs.io/manual/markdown/
- https://ablog.readthedocs.io/
- https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_sidebars
- https://sphinx.silverrainz.me/isso/



