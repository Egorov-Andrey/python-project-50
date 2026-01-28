def format_json(diff):
    """Форматирует в JSON виде."""
    import json
    return json.dumps(diff, indent=2, ensure_ascii=False)

