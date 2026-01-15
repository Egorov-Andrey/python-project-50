from pathlib import Path

from gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_generate_diff_json():
    expected = read_file("result.txt")
    actual = generate_diff("./tests/test_data/file1.json",
                            "./tests/test_data/file2.json")
    assert actual == expected
    

def test_generate_diff_yml():
    expected = read_file("result.txt")
    actual = generate_diff("./tests/test_data/file1.yml",
                            "./tests/test_data/file2.yml")
    assert actual == expected


def test_generate_diff_json1():
    expected = read_file("result1.txt")
    actual = generate_diff("./tests/test_data/file3.json",
                            "./tests/test_data/file4.json")
    assert actual == expected


def test_generate_diff_yml1():
    expected = read_file("result1.txt")
    actual = generate_diff("./tests/test_data/file3.yml",
                            "./tests/test_data/file4.yml")
    assert actual == expected