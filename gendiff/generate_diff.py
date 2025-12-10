import json


def generate_diff(filepath1, filepath2):  

    filepath1 = '/home/aegorov/projects-python/python-project-50/gendiff/file1.json'
    filepath2 = '/home/aegorov/projects-python/python-project-50/gendiff/file1.json'
    data1 = json.load(open(filepath1))
    data2 = json.load(open(filepath2))

    def format_value(value):
        if isinstance(value, bool):
            return str(value).lower()
        return str(value)
    
    result_lines = []
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    
    for key in all_keys:
        if key not in data2:
            result_lines.append(f"- {key}: {format_value(data1[key])}")
        elif key not in data1:
            result_lines.append(f"+ {key}: {format_value(data2[key])}")
        elif data1[key] != data2[key]:
            result_lines.append(f"- {key}: {format_value(data1[key])}")
            result_lines.append(f"+ {key}: {format_value(data2[key])}")
        else:
            result_lines.append(f"  {key}: {format_value(data1[key])}")
    
    return "\n".join(result_lines)
    