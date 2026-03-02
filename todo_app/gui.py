#Import the FreeSimpleGUI library and Reference it with Variable SG
from cProfile import label

import functions
import FreeSimpleGUI as sg
import time
import os

#Create a .txt file if one does not exist
if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

# E.g. sg.theme("DarkPurple4")
sg.theme("Black")

#Widget Type Label creates a label Instruction
clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")

#Widget Type Input_box creates an input box to add text to-do
#The key to-do corresponds to the value of the input box
input_box = sg.InputText(tooltip="Enter todo", key="todo")

#Widget Type Add_button creates a button to add to-do item
add_button = sg.Button(size=1,
                       image_source='add.png',
                       mouseover_colors='LightBlue',
                       tooltip='Add Todo',
                       key='Add')

#Widget Type List_box creates gets a list from the to-do.txt file, specifies the key, size & enable events
#The key to-dos corresponds to the value of the list box
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])

#Widget Type Edit_button creates a button to edit a to-do item
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

#Widget Type Window creates the application window with title.
window = sg.Window('My To-Do App',
                   #Each item in the Layout list [] represents a row or a new line
                   #Each item inside the list in the Layout list [[a, b]] are represented side by side
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   #Create a Tuple called Font and specify a font and size
                   font=('Helvetica', 20))

#Use a while loop to add and reference the get and write to-do functions from functions.py
while True:
    #event produces the result of whatever the user adds in the input box
    #values is a dictionary that produces the output or choice of to-do the user has specified or selected
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                #Use the popup function to popup the message
                sg.popup("Please select an item.", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                #Use the popup function to popup the message
                sg.popup("Please select an item.", font=("Helvetica", 20))

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()