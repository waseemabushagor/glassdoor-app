install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py python_library

format:
	black *.py python_library/*.py

all: install lint test format