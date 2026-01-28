def format_plain(diff, path=""):
    """Форматирует в простом текстовом виде."""
    result_lines = []
    
    for key, info in diff.items():
        current_path = f"{path}.{key}" if path else key
        
        if info['type'] == 'nested':
            result_lines.append(format_plain(info['children'], current_path))
        elif info['type'] == 'added':
            value = format_value_plain(info['value'])
            result_lines.append(f"Property '{current_path}'"
                                f" was added with value: {value}")
        elif info['type'] == 'removed':
            result_lines.append(f"Property '{current_path}' was removed")
        elif info['type'] == 'changed':
            old_value = format_value_plain(info['old_value'])
            new_value = format_value_plain(info['new_value'])
            result_lines.append(
                f"Property '{current_path}' was updated. From "
                f"{old_value} to {new_value}"
            )  
    
    return "\n".join(result_lines)


def format_value_plain(value):
    """Вспомогательная функция для форматирования значений в plain формате."""
    if isinstance(value, dict) or isinstance(value, list):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)