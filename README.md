# Forage lyft car service management.

A software to help manage servicing of cars at Lyft.

# Technologies and Frameworks.

1. Python programming language, annotations in Python.
1. Test Driven Development (TDD), Unit testing.
1. Python virtual environment.
1. Linting; autopep8, pycodestyle.

# Design patterns.

Factory creational design pattern.

# Linting.

## Linting using pycodestyle.

```bash
# Install pycodestyle.
pip install pycodestyle

# Confirm install.
pycodestyle --version

# Lint file.
pycodestyle <FILE>
```

## Linting using autopep8.

```bash
# Lint a file.
autopep8 --in-place <FILE>

autopep8 --in-place tests/test_engines/test_capulet_engine.py

# Lint all files in folder.
autopep8 --in-place --recursive <FOLDER>/*

autopep8 --in-place --recursive tests/*

# Lint all files in project.
autopep8 --in-place --recursive .
```

# Typing/ Annotations using mypy.
```bash
# Check typing for a file.
mypy <PYTHON_FILE>

mypy tests/test_engines/test_capulet_engine.py

mypy tests

# Check typing for all files.
mypy .
```


# Test Driven Development.

# Unit testing.

```bash
# Run all tests in test directory.
python3 -m unittest discover tests
```

# Python packages.

# requirements.txt file.

```bash
# Generate requirements file.
pip freeze > requirements.txt

# Install all packages in requirements file.
pip install -r requirements.txt
```

## virtualenv.

A tool for creating isolated virtual python environments.

```bash
# Install virtualenv in ubuntu.
sudo apt install python3-venv

# Confirm installation of virtualenv
python3 -m venv --help

# Create a new virtual environment called venv
python -m venv venv

# Activate virtual environment.
source venv/bin/activate

#Deactivate virtual environment.
Deactivate
```

[https://pypi.org/project/virtualenv/](https://pypi.org/project/virtualenv/)

## pycodestyle.

A tool to check Python code against some of the style conventions in PEP 8.

```bash
# Install pycodestyle.
pip install pycodestyle

# Confirm install.
pycodestyle --version

# Lint a file.
pycodestyle <FILE>
```

[https://pypi.org/project/pycodestyle/](https://pypi.org/project/pycodestyle/)

## autopep8.

Automatically formats Python code to conform to the PEP 8 style guide. I

```bash
# Install pycodestyle.
pip install --upgrade autopep8

# Confirm install.
autopep8 --version

# Lint a file.
autopep8 --in-place <FILE>

autopep8 --in-place tests/test_engines/test_capulet_engine.py

# Lint all files in folder.
autopep8 --in-place --recursive <FOLDER>/*

autopep8 --in-place --recursive tests/*

# Lint all files in project.
autopep8 --in-place --recursive .
```

[https://pypi.org/project/pycodestyle/](https://pypi.org/project/pycodestyle/)


## mypy.

A toold to check type annotations for Python programs.

```bash
# Install pycodestyle.
pip install mypy

# Confirm install.
mypy --version
```

# Quick commands.
```bash
# Check tests.
python3 -m unittest discover tests
mypy tests
autopep8 --in-place --recursive tests/*
```
