# Pants example

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

## Links

[Pants docs][900]

[900]: https://www.pantsbuild.org/docs



