NODE_VER := $(shell node -v | cut -c2- | cut -d. -f1 )
NODE_CHECK := $(shell if [ $(NODE_VER) = "11" ]; then echo true; else echo false; fi)

YARN_VER := $(shell yarn -v | cut -d. -f1,2 )
YARN_CHECK := $(shell if [ $(YARN_VER) = "1.19" ]; then echo true; else echo false; fi)


default: check
	yarn install

runserver:
	yarn run server

.PHONY: build
build:
	yarn run build

.PHONY: build-prod
build-prod:
	yarn run build-prod

.PHONY: check
check:
	@echo Requires Node 11.x or higher. You have $(shell node -v) && $(NODE_CHECK)
	@echo Requires Yarn 1.19.x or higher. You have $(shell yarn -v) && $(YARN_CHECK)
	echo "all good. :) "

