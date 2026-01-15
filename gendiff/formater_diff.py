def format_diff(diff, format_name='stylish'):
    """
    Форматирует внутреннее представление разницы.
    
    Args:
        diff: внутреннее представление разницы
        format_name: формат вывода ('stylish', 'plain', 'json')
    
    Returns:
        str: отформатированная строка
    """
    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plain(diff)
    elif format_name == 'json':
        return format_json(diff)
    else:
        raise ValueError(f'Unsupported format: {format_name}')


def format_stylish(diff, depth=0):
    """Форматирует в стильном виде (как в примере)."""
    indent = ' ' * (depth * 4)
    result_lines = []
    
    for key, info in diff.items():
        if info['type'] == 'nested':
            result_lines.append(f"{indent}    {key}: {{")
            result_lines.append(format_stylish(info['children'], depth + 1))
            result_lines.append(f"{indent}    }}")
        elif info['type'] == 'added':
            result_lines.append(f"{indent}  + {key}: "
                                f"{format_value(info['value'], depth + 1)}")
        elif info['type'] == 'removed':
            result_lines.append(f"{indent}  - {key}: "
                                f"{format_value(info['value'], depth + 1)}")
        elif info['type'] == 'changed':
            result_lines.append(f"{indent}  - {key}: "
                                f"{format_value(info['old_value'], depth + 1)}")
            result_lines.append(f"{indent}  + {key}: "
                                f"{format_value(info['new_value'], depth + 1)}")
        else:  # unchanged
            result_lines.append(f"{indent}    {key}: "
                                f"{format_value(info['value'], depth + 1)}")
    
    result = "\n".join(result_lines)
    
    if depth == 0:
        return "{\n" + result + "\n}"
    return result


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
                                f"was added with value:{value}")
        elif info['type'] == 'removed':
            result_lines.append(f"Property '{current_path}' was removed")
        elif info['type'] == 'changed':
            old_value = format_value_plain(info['old_value'])
            new_value = format_value_plain(info['new_value'])
            result_lines.append(
                f"Property '{current_path}' was updated. From"
                f"{old_value} to {new_value}"
            )  
    
    return "\n".join(result_lines)


def format_json(diff):
    """Форматирует в JSON виде."""
    import json
    return json.dumps(diff, indent=2, ensure_ascii=False)


def format_value(value, depth=0):
    """Вспомогательная функция для форматирования значений в stylish формате."""
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        # Рекурсивно форматируем вложенный словарь
        indent = ' ' * (depth * 4)
        lines = ['{']
        for k, v in sorted(value.items()):
            lines.append(f"{indent}    {k}: {format_value(v, depth + 1)}")
        lines.append(f"{indent}}}")
        return "\n".join(lines)
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        return str(value)


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