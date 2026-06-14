from gendiff.formatters.formatter_selection import formatter_selection
from gendiff.scripts.build_diff import build_diff
from gendiff.scripts.parser import parse_data_from_file


def generate_diff(file_path1, file_path2, formatter='stylish'):
    data1 = parse_data_from_file(file_path1)
    data2 = parse_data_from_file(file_path2)
    diff = build_diff(data1, data2)
    return formatter_selection(diff, formatter)
