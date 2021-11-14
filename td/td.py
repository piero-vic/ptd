import typer
from rich.console import Console

from db import get_list_file


app = typer.Typer(add_completion=False)
console = Console()

ok_sign = "✓"
ko_sign = "✕"


@app.command()
def main():
    """
    Show the list.
    """
    print()
    for item in get_list_file():
        if item["status"] == "pending":
            console.print(f"{item['id']} | [red]{ko_sign}[/red] {item['desc']}")
        else:
            console.print(f"{item['id']} | [green]{ok_sign}[/green] {item['desc']}")
    print()


if __name__ == "__main__":
    app()
