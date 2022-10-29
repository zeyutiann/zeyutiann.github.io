
.. Jacob's blog post example, created by `ablog start` on Oct 06, 2022.

.. post:: 2022.09.30
   :tags: githubpage, sphinx, tutorial
   :category: Documentation
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

    # adding bokeh dependencies
    poetry add bokeh-plot
    poetry add Ipython
    poetry add pandas
    poetry add matplotlib
    # adding sphinx_charts
    poetry add sphinx_charts
    poetry add jupyter-sphinx

    # ablog
    ablog start
    ablog build
    # note that ablog deploy function is not used for this project as the use-case for the deploy function is very strict, and the author didn't get it working. So the deployment is done manually by adding .nojekyll and index.html file.

    # at root folder, create new files/folders for github page
    touch .nojekyll
    touch index.html
    echo "<meta http-equiv=\"refresh\" content=\"0; url=./_website/index.html\" />" > index.html
    mkdir blog
    mkdir blog/2022-10/

    # initialise your git
    git init
    git add -A
    git commit -m "first commit"
    git branch -M main
    git remote add origin git@github.com:zeyutiann/zeyutiann.github.io.git
    git push -u origin main
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

bokeh support
==============

After installing bokeh-plot from poetry. Add below to conf.py.

.. code-block:: shell

    extension = [
        ...,
    'bokeh.sphinxext.bokeh_plot',
        ...
    ]

The bokeh-plot directive can be used by either supplying

- a path to a source file as the argument to the directive

.. code-block:: rst

    .. bokeh-plot:: path/to/plot.py

- inline code as the content of the directive:

.. code-block:: rst

    .. bokeh-plot::
        :source-position: below
        :linenos:
        :process-docstring:

        from bokeh.plotting import figure, output_file, show

        output_file("example.html")

        x = [1, 2, 3, 4, 5]
        y = [6, 7, 6, 4, 5]

        p = figure(title="example", plot_width=300, plot_height=300)
        p.line(x, y, line_width=2)
        p.circle(x, y, size=10, fill_color="white")

        show(p)

This directive also works in conjunction with Sphinx autodoc, when used in docstrings.

The bokeh-plot directive accepts the following options:

- process-docstring : bool
    Whether to display the docstring in a formatted block separate from the source.

- source-position : enum(‘above’, ‘below’, ‘none’)
    Where to locate the the block of formatted source code (if anywhere).

- linenos : bool
    Whether to display line numbers along with the source.


How to use Sphinx-charts
=========================
If you don’t know how to use plot.ly you won’t get very far with sphinx_charts!
Plots need to be saved to a JSON file, whose contents are compatible with plot.ly’s json chart schema.

.. code-block:: rst

    .. chart:: charts/test.json

        This is the caption of the chart


Jupyter Notebook
=================

or checkout jupyter-sphinx to render plotly from jupyter notebook:

.. code-block:: shell

    [...,
    'jupyter_sphinx',
    ...]


.. code-block::

    .. jupyter-execute::

        name='word'
        print(name)

Another jupyter notebook tools
- https://github.com/spatialaudio/nbsphinx

And another one
- https://github.com/QuantEcon/sphinxcontrib-jupyter
- https://sphinxcontrib-jupyter.readthedocs.io/en/latest/?badge=latest

How to use Ablog
==================

postlist
---------
.. code-block::

    .. postlist:: 5

       :author: Ahmet
       :category: Manual
       :location: Pittsburgh
       :language: en
       :tags: tips
       :date: %A, %B %d, %Y
       :format: {title} by {author} on {date}
       :list-style: circle
       :excerpts:
       :sort:
       :expand: Read more ...

* list-style: circle, disc, and none (default) are recognized.

- https://ablog.readthedocs.io/manual/posting-and-listing/


How to use Confluence
=======================
To set up, this requires Python package sphinxcontrib-confluencebuilder,similarly add it to extensions list in conf.py.
In Confluence, retrieve the space key from Space Settings > Manage space > Space details and create an API token
here <https://id.atlassian.com/manage-profile/security/api-tokens>_.
You now have all the details to publish the Sphinx documentation on Confluence!

How to use Mermaid:
====================
- https://mermaid-js.github.io/mermaid/#/README

How to copy code from code block
==================================
- https://github.com/executablebooks/sphinx-copybutton

reference:
===========

- https://documentation-style-guide-sphinx.readthedocs.io/en/latest/
- https://ablog.readthedocs.io/manual/markdown/
- https://ablog.readthedocs.io/
- https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_sidebars
- https://sphinx.silverrainz.me/isso/
- https://docs.bokeh.org/en/latest/docs/reference/sphinxext.html?highlight=sphinx#module-bokeh.sphinxext.bokeh_plot
- https://sphinx-charts.readthedocs.io/en/latest/index.html
- https://zhuanlan.zhihu.com/p/148748125
- https://jupyter-sphinx.readthedocs.io/en/latest/#
- https://sphinxcontrib-confluencebuilder.readthedocs.io/en/stable/
- https://pythonhosted.org/sphinxcontrib-exceltable/
- https://github.com/spatialaudio/nbsphinx
- https://nbsphinx.readthedocs.io/en/0.8.9/
- https://github.com/executablebooks/sphinx-tabs
- https://mermaid-js.github.io/mermaid/#/README
- https://stackoverflow.com/questions/23211695/modifying-content-width-of-the-sphinx-theme-read-the-docs




