import json
import os
from enum import Enum


class ObjectType(Enum):
    VIDEO = "videos"
    PLAYLIST = "playlists"


def read_json_file(file_path: str, category_name: str, object_type: ObjectType) -> list:
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, "r") as file:
            parsed_data = json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from file {file_path}: {e}")

    if category_name not in parsed_data:
        raise KeyError(f"Category '{category_name}' not found in JSON data.")
    if object_type.value not in parsed_data[category_name]:
        raise KeyError(
            f"Object type '{object_type.value}' not found under category '{category_name}'."
        )

    data = parsed_data[category_name][object_type.value]

    return data
