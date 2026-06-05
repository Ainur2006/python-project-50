install:
	uv sync

diff:
	uv run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

check:
	uv run ruff check .

pytest:
	uv run pytest --cov=gendiff --cov-report=xml