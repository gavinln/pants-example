# Pants example

The Pants build system multiple programming languages including Go, Java, Python, Scala, Kotlin, and Shell scripts. It is easy to adopt, use, and extend. With minimal BUILD file metadata/boilerplate, Pants can infer most of the dependency information on its own. It has a rich plugin API for customization and seamless integration with Git.

Pants works best with a monorepo architecture, containing multiple projects—often using multiple programming languages in a single unified repository. To speed up execution, Pants supports concurrent and remote execution and shared result caching.

Pants supports the following Python tools out of the box

* pytest - framework to write and execute small, readable tests
* black - a code fast code formatter that is deterministic
* yapf - a Python formatter from Google (not official product)
* flake8 - a tool to enforce the Python style guide
* docformatter - automatically formats docstrings
* pydocstyle - checks compliance with Python docstring conventions
* isort - sorts Python imports alphabetically and into sctions
* pylint - static code analyzer that checks for erros and enforces standards
* bandit - find common security issues
* autoflake - removes unused imports and unused variables
* pyupgrade - upgrades syntax to newer versions of Python
* MyPy - static type checker that catches type-related bugs
* setuptools - package development and distribution utility
* pex - creates executable Python environments that bundles dependencies
* PyOxidizer - packaging and distribution utility that embeds Python
* IPython - interactive shell for Python with enhanced functionality

[Pants github][100]

[100]: https://github.com/pantsbuild/pants

## Setup Pants

### Windows Subsystem for Linux

Install the pre-requisites

```
sudo apt install zip python3-dev python3-distutils python3-venv gcc
```

### Install Pants

```
curl --proto '=https' --tlsv1.2 -fsSL https://static.pantsbuild.org/setup/get-pants.sh | bash
```

### Run Pants goals

1. Kill pants daemon before starting using kill -9 pid

```
ps aux | grep pantsd
```

1. Display help

```
pants help
```

2. Display goals

```
pants help goals
```

3. List targets (none will be initially displayed)

```
pants list
```

4. Check before creating the BUILD files

```
pants tailor :: --tailor-check
```

5. Auto-generate BUILD files using "pants tailor ::". May not be correct

6. Generate lockfiles - typically python-default.lock

```
pants generate-lockfiles
```

7. Run tests

```
pants test ::
```

8. Create a package

```
pants package ::
```

9. Lint code

```
pants lint ::
```

### Use Pants virtualenv with an IDE

1. Export a virtualenv

```
pants export --py-resolve-format=symlinked_immutable_virtualenv --resolve=python-default
```

2. Activate the virtualenv

```
source dist/export/python/virtualenvs/python-default/3.10.12/bin/activate
```

3. Start neovim

```
nvim python-example-file.py
```

4. Deactivate the environment

```
deactivate
```

## Setup Poetry

### Setup `hello_name` project

1. List current pyenv version and location of Python executable

```
pyenv version; pyenv which python
```

2. Change to `hello_name` packages directory

```
cd py-poetry/hello_name
```

3. Setup Python for Poetry environment

```
poetry env use <PYTHON-EXECUTABLE>
```

4. Create a Poetry environment

```
poetry run python -V
```

5. Run Python code

```
poetry run python -c "from hello_name.hello_name import greet; print(greet('John'))"
```

6. Add pytest

```
poetry add pytest
```

7. Run pytest

```
poetry run pytest
```

### Setup `hello_world` project

1. List current pyenv version and location of Python executable

```
pyenv version; pyenv which python
```

2. Change to `hello_world` packages directory

```
cd py-poetry/hello_world
```

3. Setup Python for Poetry environment

```
poetry env use <PYTHON-EXECUTABLE>
```

4. Create a Poetry environment

```
poetry run python -V
```

5. Add third party dependency

```
poetry add colorama
```

6. Add local dependency

```
poetry add ../hello_name
```

7. Run Python code

```
poetry run python -c "from hello_world.hello_world import greet; print(greet())"
poetry run python -c "from hello_world.hello_world import *; print_greet()"
```

## Links

[Pants docs][900]

[900]: https://www.pantsbuild.org/docs
