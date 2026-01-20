install:
	uv sync

gendiff:
	uv run gendiff first_file second_file

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check gendiff

test:
	uv run pytest tests/

test-coverage:
	uv run pytest --cov=gendiff --cov-report=term-missing --cov-report=xml

install-test:
	uv add --dev pytest pytest-cov

