install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py python_library

test:
	python -m pytest -vv --cov=python_library test_*.py

format:
	black *.py python_library/*.py

all: install lint test format