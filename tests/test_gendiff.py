import argparse
import sys
from io import StringIO
from unittest.mock import patch, mock_open, MagicMock
from gendiff.scripts.gendiff import create_parser, run_cli, main

def test_create_parser():

    parser = create_parser()
    assert isinstance(parser, argparse.ArgumentParser)
    assert parser.description == 'Compares two configuration files and shows a difference'

def test_parser_with_format():

    parser = create_parser()

    args = parser.parse_args([
        'file1.json',
        'file2.json',
        '--format', 'plain'
    ])
    assert args.first_file == 'file1.json'
    assert args.second_file == 'file2.json'
    assert args.format == 'plain'

def test_parser_short_format():
    parser = create_parser()

    args = parser.parse_args([
        'file1.json',
        'file2.json',
        '-f', 'json'
    ])
    assert args.format == 'json'

def test_help_output():
    parser = create_parser()

    help_output = StringIO()
    parser.print_help(file=help_output)
    help_text = help_output.getvalue()

    assert 'usage' in help_text
    assert 'first_file' in help_text
    assert 'second_file' in help_text
    assert '--format' in help_text
    assert 'stylish' in help_text
    assert 'plain' in help_text
    assert 'json' in help_text

