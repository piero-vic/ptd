import typer
from datetime import datetime
import time
from typing import Optional
from .db import init_db, get_list_file, get_task_index, write_to_file


app = typer.Typer()
OK_SIGN = typer.style("✓", fg=typer.colors.GREEN, bold=True)
KO_SIGN = typer.style("✕", fg=typer.colors.RED, bold=True)


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    To Do list for the command line.
    """
    if ctx.invoked_subcommand is None:
        list = get_list_file()
        if list:
            print()
            for item in list:
                space_num = 6 - len(str(item["id"]))
                if item["status"] == "pending":
                    typer.echo(
                        f"{space_num*' '}{item['id']} | {KO_SIGN} {item['desc']}"
                    )
                else:
                    typer.echo(
                        f"{space_num*' '}{item['id']} | {OK_SIGN} {item['desc']}"
                    )
            print()
        else:
            typer.secho("There are no tasks to show.", fg=typer.colors.CYAN)


@app.command()
def init():
    """
    Initialize a collection of todos.
    """
    init_db()


@app.command()
def add(desc: str):
    """
    Add a new task to the list.
    """
    list = get_list_file()
    if list:
        id = list[-1]["id"] + 1
    else:
        id = 1

    new_item = {
        "id": id,
        "desc": desc,
        "status": "pending",
        "modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f ")
        + time.strftime("%z %Z", time.localtime()),
    }

    list.append(new_item)
    write_to_file(list)
    typer.secho(f'#{id} "{desc}" is now added to your todos.', fg=typer.colors.CYAN)


@app.command()
def modify(id: int = typer.Argument(...), desc: str = typer.Argument(...)):
    """
    Modify the text of an existing task.
    """
    list = get_list_file()
    index = get_task_index(id, list)
    list[index]["desc"] = desc
    write_to_file(list)
    typer.secho(f"#{id} has now a new description: {desc}", fg=typer.colors.CYAN)


@app.command()
def toggle(id: int = typer.Argument(...)):
    """
    Toggle the status of a task by giving his id.
    """
    list = get_list_file()
    index = get_task_index(id, list)
    status = list[index]["status"]
    if status == "pending":
        list[index]["status"] = "done"
    else:
        list[index]["status"] = "pending"
    write_to_file(list)
    typer.secho(f'Your todo is now {list[index]["status"]}.', fg=typer.colors.CYAN)


@app.command()
def clean():
    """
    Remove finished tasks from the list.
    """
    list = get_list_file()
    list = [task for task in list if task["status"] == "pending"]
    write_to_file(list)
    typer.secho("Your list is now flushed of finished todos.", fg=typer.colors.CYAN)


@app.command()
def reorder(
    id_1: Optional[int] = typer.Argument(None),
    id_2: Optional[int] = typer.Argument(None),
):
    """
    Reset ids of todo (no arguments) or swap the position of two todos.
    """
    list = get_list_file()
    if id_1 is None or id_2 is None:
        for index, item in enumerate(list, start=1):
            item["id"] = index
        typer.secho("Your list is now ordered.", fg=typer.colors.CYAN)
    else:
        item_1 = [task for task in list if task["id"] == id_1][0]
        item_2 = [task for task in list if task["id"] == id_2][0]

        index_1 = list.index(item_1)
        index_2 = list.index(item_2)

        item_1["id"] = id_2
        item_2["id"] = id_1

        list[index_1] = item_2
        list[index_2] = item_1

        typer.secho("Your tasks have been swapped.", fg=typer.colors.CYAN)

    write_to_file(list)


if __name__ == "__main__":
    app()
