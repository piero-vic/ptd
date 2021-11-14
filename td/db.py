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
    except:
        print("No config file")
