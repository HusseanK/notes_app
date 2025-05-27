import json


def return_data_as_dict(file_path: str) -> dict:
    with open(file_path, "r") as f:
        data = json.load(f)
    return data