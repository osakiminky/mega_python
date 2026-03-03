import os

# Get absolute path of current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILEPATH = os.path.join(BASE_DIR, "todos.txt")

# FILEPATH = "../todo_web_app/todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read the text file and return a list of todos """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def  write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items in the text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == '__main__':
    print("Hello\nThese are the available tasks to do!")
    print(get_todos())