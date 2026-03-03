FILEPATH = "../todo_web_app/todos.txt"

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