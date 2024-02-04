FILEPATH = "todos.txt"  # bien hang so - thuong duoc khai bao trong module (de module va c/tr chinh co the su dung khi import module)


def get_todos(filepath=FILEPATH):    # parameter "filepath" in fucntion definition
    # khai bao phan docstrings cua ham "get_todos"
    """ Read the "todo" text file and
    return "todos" to a list
    """
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the "todos" list to "todo" text file. """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)



