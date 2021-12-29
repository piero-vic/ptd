import os
import json
import typer


HOME_DIR = os.environ['HOME']
TODO_DB = f"{HOME_DIR}/.todos"


def init_db():
    if os.path.isfile(TODO_DB):
        typer.secho("The file has already been created.", fg=typer.colors.CYAN)
    else:
        f = open(TODO_DB, "w+")
        f.close()
        typer.secho("New file created", fg=typer.colors.CYAN)


def get_list_file():
    try:
        if os.path.getsize(TODO_DB) == 0:
            return []
        else:
            with open(TODO_DB, 'r') as file:
                return json.load(file)
    except Exception as e:
        typer.echo(
            f'{typer.style("Error", fg=typer.colors.RED)}\n'
            'A store for your todos is missing.\n'
            'Create a ".todos" file in your home directory.'
        )
        exit()


def get_task_index(id, list):
    task = [task for task in list if task["id"] == id][0]
    return list.index(task)


def write_to_file(file_data):
    with open(TODO_DB, 'w') as file:
        json.dump(file_data, file, indent=2)
