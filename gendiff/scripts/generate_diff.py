import json

import yaml

from gendiff.formaters.format_diff import format_diff
from gendiff.scripts.differ import build_diff


def load_data(filepath):
    with open(filepath, 'r') as f:
        if filepath.endswith('.json'):
            return json.load(f)
        elif filepath.endswith(('.yaml', '.yml')):
            return yaml.safe_load(f)
        else: 
            raise ValueError(f'Unsupported file format: {filepath}')
        

def generate_diff(filepath1, filepath2, format_name='stylish'):
  
    data1 = load_data(filepath1)
    data2 = load_data(filepath2)

    diff_tree = build_diff(data1, data2)
        
    return format_diff(diff_tree, format_name)