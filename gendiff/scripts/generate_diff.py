from gendiff.formatters.stylish import format_diff_stylish
from gendiff.scripts.build_diff import build_diff
from gendiff.scripts.parser import parse_data_from_file


def generate_diff(file_path1, file_path2):
    data1 = parse_data_from_file(file_path1)
    data2 = parse_data_from_file(file_path2)
    diff = build_diff(data1, data2)
    return format_diff_stylish(diff)
