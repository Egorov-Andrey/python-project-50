from gendiff.formaters.format_json import format_json
from gendiff.formaters.format_plain import format_plain
from gendiff.formaters.format_stylish import format_stylish


def format_diff(diff, format_name='stylish'):

    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    else:
        raise ValueError(f'Unsupported format: {format_name}')
    
