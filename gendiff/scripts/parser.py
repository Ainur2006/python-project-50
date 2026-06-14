import json
from pathlib import Path

import yaml


def parse_data_from_file(file_path):
    file_format = Path(file_path)

    yaml_suffix = ('.yaml', '.yml')

    if file_format.suffix == '.json':
        data = json.load(open(file_path))
    elif file_format.suffix in yaml_suffix:
        data = yaml.safe_load(open(file_path))

    return data
    


    