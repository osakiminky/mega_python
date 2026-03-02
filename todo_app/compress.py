import FreeSimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
#Create a key called files that will reference the output of the values after an event below
choose_button1 = sg.FileBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                            [compress_button, output_label]
                           ])
#Create a while loop
while True:
    #We need to read the events all the time and get the values
    event, values = window.read()
    print(event, values)
    #Specify the key that outputs a value anytime the choose_button calls Choose
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed!")

window.close()