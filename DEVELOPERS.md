Project setup
=============

This project uses Poetry for dependency management:

Install Poetry:
```sh
$ curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
```

Create a venv:
```sh
$ python3 -mvenv toybot-env
```

Activate the venv
```sh
$ source toybot-env/bin/activate
```

Install dependencies using Poetry
```sh
$ poetry up
```

Install toybot

```sh
$ poetry install
```


IDE Setup
=========

.editorconfig is provided.

To have the best chance of landing code is advisable to get your editor
to run the following tools on save:

 - flake8
 - black
 - isort


Formatting
==========

Black

[Black](https://black.readthedocs.io/en/stable/) is used for formatting.

Editors can usually be setup to run it on save.

Our pre-commit hook can be used to check formatting is consistent.


Linting
-------

Flake8 is used to find common errors.
Line width is set to 88 characters for compatiblity with Black.


pre-commit hook 


Testing
=

Testing uses pytest
=

Run tests:

```sh
$ pytest 
```

Tests adhere to AAA

- Arrange
- Act
- Assert

Test Coverage
=

[pytest-cov](https://pytest-cov.readthedocs.io) is used to check test coverage:

```sh
$ pytest --cov=toybot tests
```


Docs
=

Sphinx

Sphinx Settings

Markdown used by default.


API Docs
--------

API docs + sphinx

Format:  The numpy format is used.
