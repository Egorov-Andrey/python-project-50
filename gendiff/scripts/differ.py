def build_diff(node1, node2):
    """
    Рекурсивно строит внутреннее представление разницы между двумя узлами.
    
    Args:
        node1: первый словарь/узел
        node2: второй словарь/узел
    
    Returns:
        dict: внутреннее представление разницы
    """
    diff = {}
    
    all_keys = sorted(set(node1.keys()) | set(node2.keys()))
    
    for key in all_keys:
        value1 = node1.get(key)
        value2 = node2.get(key)
        
        if key not in node1:
            diff[key] = {
                'type': 'added',
                'value': value2
            }

        elif key not in node2:
            diff[key] = {
                'type': 'removed',
                'value': value1
            }

        elif value1 == value2:
            diff[key] = {
                'type': 'unchanged',
                'value': value1
            }

        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = {
                'type': 'nested',
                'children': build_diff(value1, value2)
            }

        else:
            diff[key] = {
                'type': 'changed',
                'old_value': value1,
                'new_value': value2
            }

    return diff