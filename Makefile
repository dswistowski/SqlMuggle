.PHONY: format lint test black black-lint ruff ruff-lint pytest mypy

format: black ruff

lint: black-lint ruff-lint mypy

test:  pytest

black:
	poetry run black .

black-lint:
	poetry run black --check .

ruff:
	poetry run ruff --format=github .

ruff-lint:
	poetry run ruff check --format=github .

pytest:
	poetry run pytest

mypy:
	poetry run mypy -p sqlmuggle --install-types --non-interactive
