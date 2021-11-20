# todo
> A minimal todo list for your terminal.

## Installation

Run the following command.

```
pip install git+https://github.com/piero-vic/todo.git
```

## Usage

*todo* will search for a `.todos` file inside your home directory. All the tasks are stored as JSON objects.

### CLI

```
Usage: todo [OPTIONS] COMMAND [ARGS]...

  To Do list for the command line.

Options:
  --help  Show this message and exit.

Commands:
  add     Add a new task to the list.
  clean   Remove finished tasks from the list.
  modify  Modify the text of an existing task.
  toggle  Toggle the status of a task by giving his id.
```

## Acknowledgments
This project is mainly based on [td](https://github.com/Swatto/td). I just wanted to build it myself in a language I know.
