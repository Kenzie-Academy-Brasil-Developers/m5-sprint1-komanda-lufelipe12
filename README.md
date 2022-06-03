### First requirement Python 3.10

### use the command to create new virtual env

`python -m venv .venv`

### use the command to activate virtual env

`source .venv/bin/activate`

### use the command to install dependencies in virtual env

`pip install -r requirements.txt`

### if you modified any lib use:

`pip freeze > requirements.txt`

### to execute tests run:

`pytest tests/tests_management.py`

### to quit virtual environment use:

`deactivate`
