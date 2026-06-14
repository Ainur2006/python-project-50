def add(key, value):
    return {
        'action': 'added',
        'name': key,
        'new_value': value
    }


def delete(key, value):
    return {
        'action': 'deleted',
        'name': key, 
        'old_value': value
    }


def unchanged(key, value):
    return {
        'action': 'unchanged',
        'name': key,
        'value': value
    }


def update(key, value1, value2):
    return {
        'action': 'updating',
        'name': key,
        'old_value': value1,
        'new_value': value2
    }


def nested(key, value1, value2):
    return {
        'action': 'nested',
        'name': key,
        'children': build_diff(value1, value2)
    }


def build_diff(data1, data2):
    all_keys = sorted(data1.keys() | data2.keys())

    diff = []

    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key in data1 and key not in data2:
            diff.append(delete(key, value1))
        elif key not in data1 and key in data2:
            diff.append(add(key, value2))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(nested(key, value1, value2))
        elif value1 != value2:
            diff.append(update(key, value1, value2))
        else:
            diff.append(unchanged(key, value1)) 

    return diff

