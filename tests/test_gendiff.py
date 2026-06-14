from pathlib import Path

from gendiff.scripts.gendiff import generate_diff


def test_stylish_formatter_json():
    expected = Path(
        "tests/fixtures/stylish_result.txt"
    ).read_text()

    result = generate_diff(
        "tests/fixtures/file1.json",
        "tests/fixtures/file2.json",
    )

    assert result == expected


def test_stylish_formatter_yaml():
    expected = Path(
        "tests/fixtures/stylish_result.txt"
    ).read_text()

    result = generate_diff(
        "tests/fixtures/file1.yml",
        "tests/fixtures/file2.yml",
    )

    assert result == expected


def test_plain_formatter_json():
    expected = Path(
        "tests/fixtures/plain_result.txt"
    ).read_text()

    result = generate_diff(
        "tests/fixtures/file1.json",
        "tests/fixtures/file2.json",
        formatter="plain",
    )

    assert result == expected


def test_plain_formatter_yaml():
    expected = Path(
        "tests/fixtures/plain_result.txt"
    ).read_text()

    result = generate_diff(
        "tests/fixtures/file1.yml",
        "tests/fixtures/file2.yml",
        formatter="plain",
    )

    assert result == expected