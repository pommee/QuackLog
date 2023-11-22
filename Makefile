IMAGE_NAME = quacklog

.PHONY: build run

build-run:
	docker build -t $(IMAGE_NAME) . && docker run -it $(IMAGE_NAME)