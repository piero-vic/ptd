import os
import json
from pathlib import Path


HOME_DIR = os.environ['HOME']
TODO_DB = Path(f"{HOME_DIR}/.todos")


def get_list_file():
    try:
        file = open(TODO_DB)
        data = json.load(file)
        return data
    except Exception as e:
        print("No config file")


def write_to_file(dict):
    if os.path.getsize(f"{HOME_DIR}/.todos") == 0:
        file_data = []
    else:
        with open(f"{HOME_DIR}/.todos", 'r') as file:
            file_data = json.load(file)

    file_data.append(dict)
    with open(f"{HOME_DIR}/.todos", 'w') as file:
        json.dump(file_data, file, indent=2)
