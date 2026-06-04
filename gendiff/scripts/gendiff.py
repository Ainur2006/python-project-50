import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )

    parser.add_argument("first_file")
    parser.add_argument("second_file")

    parser.add_argument("-f", "--format", help="set format of output")

    args = parser.parse_args()

    data1 = json.load(open(args.first_file))
    data2 = json.load(open(args.second_file))

    # print(data1)
    # print(data2)

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
            lines.append(f'  - {key}: {format_bool(data1[key])}')   # result[f'- {key}'] = data1[key]
        elif key not in data1 and key in data2:
            lines.append(f'  + {key}: {format_bool(data2[key])}')
        elif data1[key] != data2[key]:
            lines.append(f'  - {key}: {format_bool(data1[key])}')
            lines.append(f'  + {key}: {format_bool(data2[key])}')
        else:
            lines.append(f'    {key}: {format_bool(data1[key])}')

    # for i in lines:
    #     print(i)

    result = '{\n' + '\n'.join(lines) + '\n}'

    print(result)
    

def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))
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
            lines.append(f'  - {key}: {format_bool(data1[key])}')   # result[f'- {key}'] = data1[key]
        elif key not in data1 and key in data2:
            lines.append(f'  + {key}: {format_bool(data2[key])}')
        elif data1[key] != data2[key]:
            lines.append(f'  - {key}: {format_bool(data1[key])}')
            lines.append(f'  + {key}: {format_bool(data2[key])}')
        else:
            lines.append(f'    {key}: {format_bool(data1[key])}')

    result = '{\n' + '\n'.join(lines) + '\n}'

    return result