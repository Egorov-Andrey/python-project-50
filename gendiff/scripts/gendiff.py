import argparse

from gendiff.scripts.generate_diff import generate_diff


def create_parser():

    parser = argparse.ArgumentParser(description='Compares two configuration '
    'files and shows a difference')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default='stylish',
                        choices=['stylish', 'plain', 'json']
    )
    return parser


def run_cli(args=None):
    parser = create_parser()
    parsed_args = parser.parse_args(args)

    diff_result = generate_diff(
        parsed_args.first_file, 
        parsed_args.second_file,
        parsed_args.format
    )
    return diff_result


def main():

    result = run_cli()
    print(result)


if __name__ == '__main__':
    main()

