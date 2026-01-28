def format_stylish(diff, depth=0):

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