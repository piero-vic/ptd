import os
import json


HOME_DIR = os.environ['HOME']
TODO_DB = f"{HOME_DIR}/.todos-test"


def get_list_file():
    try:
        if os.path.getsize(TODO_DB) == 0:
            return []
        else:
            with open(TODO_DB, 'r') as file:
                return json.load(file)
    except Exception as e:
        print("No todo file")
        exit()


def get_task_index(id, list):
    task = [task for task in list if task["id"] == id][0]
    return list.index(task)


def write_to_file(file_data):
    with open(TODO_DB, 'w') as file:
        json.dump(file_data, file, indent=2)
