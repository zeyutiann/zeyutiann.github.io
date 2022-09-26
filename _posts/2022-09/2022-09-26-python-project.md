---
title: 'Python Project'
published: true
tags: PEP8 Poetry Git
---

### PEP8 on ASCII Compatibility: 
#### Package and Module Names
Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.

When an extension module written in C or C++ has an accompanying Python module that provides a higher level (e.g. more object oriented) interface, the C/C++ module has a leading underscore (e.g. _socket).
#### Class Names
Class names should normally use the CapWords convention.

The naming convention for functions may be used instead in cases where the interface is documented and used primarily as a callable.

Note that there is a separate convention for builtin names: most builtin names are single words (or two words run together), with the CapWords convention used only for exception names and builtin constants.


### Poetry
use poetry to create a project with a src folder at local
```commandline
poetry new --src my-package
```
Poetry assumes your package contains a package with the same name as `tool.poetry.name` located in the root of your project. If this is not the case, populate `tool.poetry.packages` to specify your packages and their locations.

Similarly, the traditional `MANIFEST.in` file is replaced by the `tool.poetry.readme`, `tool.poetry.include`, and `tool.poetry.exclude` sections. `tool.poetry.exclude` is additionally implicitly populated by your `.gitignore`. For full documentation on the project format, see the pyproject section of the documentation.

Poetry will require you to explicitly specify what versions of Python you intend to support, and its universal locking will guarantee that your project is installable (and all dependencies claim support for) all supported Python versions.

That will create a folder structure as follows:
```commandline
my-package
├── pyproject.toml
├── README.md
├── src
│   └── my_package
│       └── __init__.py
└── tests
    └── __init__.py
```


#### pyproject.toml 

```commandline
[tool.poetry]
name = "my-project"
version = "0.1.0"
description = ""
authors = ["Sébastien Eustace <sebastien@eustace.io>"]
maintainers = ["Sébastien Eustace <sebastien@eustace.io>","Sébastien Eustace Jr <sebastienjr@eustace.io>"]
readme = "README.md"
packages = [{include = "poetry_demo"}]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.7"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

#### license
the recommended notation for the most common licenses is (alphabetical):
- Apache-2.0
- BSD-2-Clause
- BSD-3-Clause
- BSD-4-Clause
- GPL-2.0-only
- GPL-2.0-or-later
- GPL-3.0-only
- GPL-3.0-or-later
- LGPL-2.1-only
- LGPL-2.1-or-later
- LGPL-3.0-only
- LGPL-3.0-or-later
- MIT
Optional, but it is highly recommended to supply this.

##### specifying dependencies 
```commandline
[tool.poetry.dependencies]
pendulum = "^2.1"
```
```commandline
poetry add pendulum
```
##### Virtual Environment 
By default, Poetry creates a virtual environment in `{cache-dir}/virtualenvs`. You can change the cache-dir value by editing the Poetry configuration. Additionally, you can use the virtualenvs.in-project configuration variable to create virtual environments within your project directory.

- `poetry run` 
  - `poetry run python your_script.py`
  - if you have command line tools such as `pytest` or `black` you can run them using `poetry run pytest`
- `poetry shell`
  - `exit`
#### managing and installing dependencies
Poetry provides a way to organize your dependencies by groups. For instance, you might have dependencies that are only needed to test your project or to build the documentation.

To declare a new dependency group, use a tool.poetry.group.<group> section where <group> is the name of your dependency group (for instance, test):
```commandline
[tool.poetry.group.test]  # This part can be left out

[tool.poetry.group.test.dependencies]
pytest = "^6.0.0"
pytest-mock = "*"
```
The dependencies declared in tool.poetry.dependencies are part of an implicit main group.
```commandline
[tool.poetry.dependencies]  # main dependency group
httpx = "*"
pendulum = "*"
[tool.poetry.group.test.dependencies]
pytest = "^6.0.0"
pytest-mock = "*"
```
Dependency groups, other than the implicit main group, must only contain dependencies you need in your development process. Installing them is only possible by using Poetry.

To declare a set of dependencies, which add additional functionality to the project during runtime, use extras instead. Extras can be installed by the end user using pip.

Any dependency declared in the dev-dependencies section will automatically be added to a dev group. So the two following notations are equivalent:

```commandline
[tool.poetry.dev-dependencies]
pytest = "^6.0.0"
pytest-mock = "*"
```

```commandline
[tool.poetry.group.dev.dependencies]
pytest = "^6.0.0"
pytest-mock = "*"

```
A dependency group can be declared as optional. This makes sense when you have a group of dependencies that are only required in a particular environment or for a specific purpose.
Optional groups can be installed in addition to the default dependencies by using the `--with` option of the install command.
Optional group dependencies will still be resolved alongside other dependencies, so special care should be taken to ensure they are compatible with each other.
```commandline
[tool.poetry.group.docs]
optional = true

[tool.poetry.group.docs.dependencies]
mkdocs = "*"
```
adding a dependency to a group
```commandline
poetry install --with docs
poetry add pytest --group test
poetry remove mydocs --group docs
```

installing dependencies 
```commandline
poetry install
poetry install --without test,docs
poetry install --with test,docs
poetry install --only test,docs
poetry install --only-root 
poetry install --sync 
poetry install --extras "mysql pgsql"
``` 
- `test, docs` are dependencies groups
- `--only-root` install the project itself with no depdendencies, skipp the installation
- `--sync` sync your enviornment, and ensure it matches the lock file
- Extras are not sensitive to `--sync`
- `--without`: The dependency groups to ignore.
- `--with`: The optional dependency groups to include.
- `--only`: The only dependency groups to include.
- `--only-root`: Install only the root project, exclude all dependencies.
- `--sync`: Synchronize the environment with the locked packages and the specified groups.
- `--no-root`: Do not install the root package (your project).
- `--dry-run`: Output the operations but do not execute anything (implicitly enables –verbose).
- `--extras` (-E): Features to install (multiple values allowed).
- `--all-extras`: Install all extra features (conflicts with –extras).
- `--no-dev`: Do not install dev dependencies. (Deprecated, use --without dev or --only main instead)
- `--remove-untracked`: Remove dependencies not presented in the lock file. (Deprecated, use --sync instead)

```commandline
poetry update
poetry update requests toml
poetry add requests pendulum 
# Allow >=2.0.5, <3.0.0 versions
poetry add pendulum@^2.0.5
# Allow >=2.0.5, <2.1.0 versions
poetry add pendulum@~2.0.5
# Allow >=2.0.5 versions, without upper bound
poetry add "pendulum>=2.0.5"
# Allow only 2.0.5 version
poetry add pendulum==2.0.5
poetry add pendulum@latest
poetry add mkdocs --group docs
poetry remove pendulum
poetry remove mkdocs --group docs
poetry show
poetry check 
poetry lock 
```
The run command executes the given command inside the project’s virtualenv.
```commandline
poetry run python -V
```
It can also execute one of the scripts defined in pyproject.toml.
```commandline
[tool.poetry.scripts]
my-script = "my_module:main"
```
```commandline
poetry run my-script
```


#### Installing a pre-existing project 
Instead of creating a new project, Poetry can be used to ‘initialise’ a pre-populated directory. To interactively create a pyproject.toml file in directory pre-existing-project
```commandline
cd my-package 
poetry init
```

#### packaging and publishing
```commandline
poetry build
poetry publish 
poetry publish -r my-repository
```

### Github
Github create new repo with the same name. 
```commandline
git init 
git add -a
git commit -m "first commit"
git branch -M main 
git remote add origin git@github.com:jacobtianzeyu/my-package.git
git push -u origin main 
```


### Reference
- [https://peps.python.org/pep-0008/#package-and-module-names](https://peps.python.org/pep-0008/#package-and-module-names)
- [https://python-poetry.org/docs/cli/](https://python-poetry.org/docs/cli/)
- [https://python-poetry.org/docs/basic-usage/](https://python-poetry.org/docs/basic-usage/)
- [https://python-poetry.org/docs/pyproject/](https://python-poetry.org/docs/pyproject/)