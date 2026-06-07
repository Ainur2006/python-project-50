import json
from pathlib import Path

import yaml


def generate_diff(file_path1, file_path2):
    file_format1 = Path(file_path1)
    file_format2 = Path(file_path2)

    y = ('.yaml', '.yml')

    if file_format1.suffix == '.json' and file_format2.suffix == '.json':
        data1 = json.load(open(file_path1))
        data2 = json.load(open(file_path2))
    elif file_format1.suffix in y and file_format2.suffix in y:
        data1 = yaml.safe_load(open(file_path1))
        data2 = yaml.safe_load(open(file_path2))

    all_keys = sorted(data1.keys() | data2.keys())

    def format_bool(value):
        if value is True:
            return 'true'
        if value is False:
            return 'false'
        return str(value)

    lines = []

    for key in all_keys:
        if key in data1 and key not in data2:
            lines.append(f'  - {key}: {format_bool(data1[key])}')
        elif key not in data1 and key in data2:
            lines.append(f'  + {key}: {format_bool(data2[key])}')
        elif data1[key] != data2[key]:
            lines.append(f'  - {key}: {format_bool(data1[key])}')
            lines.append(f'  + {key}: {format_bool(data2[key])}')
        else:
            lines.append(f'    {key}: {format_bool(data1[key])}')

    result = '{\n' + '\n'.join(lines) + '\n}'

    return result