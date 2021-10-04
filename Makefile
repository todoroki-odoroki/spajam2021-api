PACKAGE_DIR := app/

.PHONY: install
install:
	poetry install

.PHONY: update
update:
	poetry update

.PHONY: lint
lint:
	poetry run flake8 .

format:
	poerty run black .

sort:
	poetry run sort .