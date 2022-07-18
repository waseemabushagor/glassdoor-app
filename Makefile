install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py python_library

format:
	black *.py python_library/*.py
	
deploy:
	#deploy
	aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/q5e6p0b8
	docker build -t waseem .
	docker tag waseem:latest public.ecr.aws/q5e6p0b8/waseem:latest
	docker push public.ecr.aws/q5e6p0b8/waseem:latest

all: install post-install lint test format deploy