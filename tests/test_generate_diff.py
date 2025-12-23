from pathlib import Path

from gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_generate_diff():
    expected = read_file("result.txt")
    actual = generate_diff("./tests/test_data/file1.json",
                            "./tests/test_data/file2.json")
    assert actual == expected