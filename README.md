# `touchgdoc`

[![Build Status](https://travis-ci.org/jpstroop/touchgdoc.svg?branch=master)](https://travis-ci.org/jpstroop/touchgdoc)
[![Requirements Status](https://requires.io/github/jpstroop/touchgdoc/requirements.svg?branch=master)](https://requires.io/github/jpstroop/touchgdoc/requirements/?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/jpstroop/touchgdoc/badge.svg?branch=master)](https://coveralls.io/github/jpstroop/touchgdoc?branch=master)
[![Python 3.7](https://img.shields.io/badge/python-3.7-yellow.svg)](https://img.shields.io/badge/python-3.7-yellow.svg)
[![License: Simplified BSD](https://img.shields.io/badge/license-Simplified%20BSD-blue.svg)](https://github.com/jpstroop/touchgdoc/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Maintainability](https://api.codeclimate.com/v1/badges/c80d6ee046159351eba3/maintainability)](https://codeclimate.com/github/jpstroop/touchgdoc/maintainability)

## Getting Started

### Installation

Use Python 3.7 or greater.

If you do not want to develop the code and just need to run queries, install the dependencies with:

```
$ pip install -r requirements.txt
```

### Installation for Development

NB: on OS 10.X you'll need xcode: `$ xcode-select --install`

[`pipenv`](https://github.com/pypa/pipenv#installation) is used for development/debugging. After cloning, do:
```
$ pipenv --python 3.7
$ pipenv install
```
You should only need to do this the first time. Then:

To run a script, do:
```
$ pipenv run python <my_script>
```
To add a dependency (add `--dev` and/or `--pre` as necessary):
```
$ pipenv install <my_dep>
```
To remove a dependency:
```
$ pipenv uninstall <my_dep>
```
To keep `requirements.txt` in sync (run this after any dependency changes), do:
```
$ pipenv lock -r > requirements.txt
```
To update all dependencies:
```
$ pipenv update --outdated
```
Keep your environment tidy by occasionally running:
```
$ pipenv clean
```

Call `pipenv --help` or `pipenv <subcommand> --help` or see [the docs](https://github.com/pypa/pipenv#-usage) for details.

### Style

When in doubt, run [Black](https://black.readthedocs.io/en/stable/index.html):
```
$ pipenv run black -t py37 -l 79 <dirs and files>
```

Follow [Google's Style Guide](http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) for docstrings.
