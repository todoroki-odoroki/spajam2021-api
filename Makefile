PACKAGE_DIR := app/

.PHONY: install
install:
	poetry install

.PHONY: update
update:
	poetry update

.PHONY: lint
lint:
	poetry run pre-commit run --all-files