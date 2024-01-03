init:
	poetry shell
	sleep 3
	poetry install

run:
	python3 main.py

# load data from yelp fusion api for RAG local dataset
load:
	python3 main.py --load

lint:
	black .

docker-build:
	docker build -t metron .
.PHONY: docker-build

docker-run:
	docker run -it --env-file=.envrc metron
