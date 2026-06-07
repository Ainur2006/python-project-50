install:
	uv sync

diffjson:
	uv run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

diffyml:
	uv run gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml

check:
	uv run ruff check .

pytest:
	uv run pytest --cov=gendiff --cov-report=xml