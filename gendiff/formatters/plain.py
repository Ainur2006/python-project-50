PROP = "Property "
ADD = " was added with value: "
DEL = " was removed"
LINE = ' was updated. From '
LINE2 = " to "


def format_value(value):
    if value is None:
        return "null"
    
    if isinstance(value, bool):
        return str(value).lower()
    
    if isinstance(value, dict):
        return "[complex value]"
    
    if isinstance(value, str):
        return f"'{value}'"
    
    return f"{value}"


def make_plain_item(diff, path=""):
    key = diff['name']
    action = diff['action']
    new_value = format_value(diff.get('new_value'))
    old_value = format_value(diff.get('old_value'))
    current_path = f"{path}.{key}" if path else key
    
    if action == "added":
        return f"{PROP}'{current_path}'{ADD}{new_value}"
    elif action == "deleted":
        return f"{PROP}'{current_path}'{DEL}"
    elif action == "updating":
        return f"{PROP}'{current_path}'{LINE}{old_value}{LINE2}{new_value}"
    elif action == "nested":
        children = diff.get('children')
        return make_plain_diff(children, current_path)
    return None


def make_plain_diff(diff, path=""):
    lines = []
    
    for item in diff:
        line = make_plain_item(item, path)
        if line:
            lines.append(line)

    return '\n'.join(lines)


def format_diff_plain(data):
    return make_plain_diff(data)
