COMMIT_SHA := $(shell git log -1 --pretty=format:"%h")
export COMMIT_SHA

build:
	cd docker && docker build \
		--target base \
		--tag bjason01/python-iainteractive:latest \
		.

	cd docker && docker build \
		--target develop \
		--tag bjason01/python-iainteractive:develop \
		.

push: build
	docker push \
		bjason01/python-iainteractive:latest

	docker push \
		bjason01/python-iainteractive:develop
