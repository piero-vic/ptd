import typer
from datetime import datetime
import time
import json

from db import HOME_DIR
from db import TODO_DB
from db import get_list_file
from db import write_to_file


app = typer.Typer(add_completion=False)
OK_SIGN = typer.style("✓", fg=typer.colors.GREEN, bold=True)
KO_SIGN = typer.style("✕", fg=typer.colors.RED, bold=True)


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    To Do list for the command line.
    """
    if ctx.invoked_subcommand is None:
        print()
        for item in get_list_file():
            if item["status"] == "pending":
                typer.echo(f"{item['id']} | {KO_SIGN} {item['desc']}")
            else:
                typer.echo(f"{item['id']} | {OK_SIGN} {item['desc']}")
        print()


@app.command()
def add(desc: str):
    """
    Add a new task to the list.
    """
    list = get_list_file()
    id = list[-1]["id"]+1

    new_item = {
        "id": id,
        "desc": desc,
        "status": "pending",
        "modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f ") + time.strftime("%z %Z", time.localtime())
    }

    list.append(new_item)
    write_to_file(list)


@app.command()
def modify(index: int = typer.Argument(...),
           desc: str = typer.Argument(...)):
    """
    Modify the text of an existing task.
    """
    list = get_list_file()
    list[index-1]["desc"] = desc
    write_to_file(list)


@app.command()
def toggle(index: int = typer.Argument(...)):
    """
    Toggle the status of a task by giving his id.
    """
    list = get_list_file()
    status = list[index-1]["status"]
    if status == "pending":
        list[index-1]["status"] = "done"
    else:
        list[index-1]["status"] = "pending"
    write_to_file(list)


if __name__ == "__main__":
    app()
