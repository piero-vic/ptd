import typer
from rich.console import Console
from datetime import datetime
import time

from db import get_list_file
from db import write_to_file


app = typer.Typer(add_completion=False)
console = Console()
OK_SIGN = "✓"
KO_SIGN = "✕"


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    To Do list for the command line.
    """
    if ctx.invoked_subcommand is None:
        print()
        for item in get_list_file():
            if item["status"] == "pending":
                console.print(f"{item['id']} | [red]{KO_SIGN}[/red] {item['desc']}")
            else:
                console.print(f"{item['id']} | [green]{OK_SIGN}[/green] {item['desc']}")
        print()


@app.command()
def add(desc: str):
    """
    Add an item to the list.
    """
    list = get_list_file()
    id = list[-1]["id"]+1

    new_item = {
        "id": id,
        "desc": desc,
        "status": "pending",
        "modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f ") + time.strftime("%z %Z", time.localtime())
    }

    write_to_file(new_item)


if __name__ == "__main__":
    app()
