import os
import json
from pathlib import Path


HOME_DIR = os.environ['HOME']
TODO_DB = Path(f"{HOME_DIR}/.todos")


def get_list_file():
    try:
        if os.path.getsize(f"{HOME_DIR}/.todos") == 0:
            return []
        else:
            with open(f"{HOME_DIR}/.todos", 'r') as file:
                return json.load(file)
    except Exception as e:
        print("No todo file")
        exit()


def write_to_file(file_data):
    with open(f"{HOME_DIR}/.todos", 'w') as file:
        json.dump(file_data, file, indent=2)
