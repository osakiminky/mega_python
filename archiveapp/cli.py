#Import and install the FreeSimpleGUI module & libraries
import FreeSimpleGUI as sg

#Import the extract_archive function from the zip_extractor.py file
from zip_extractor import extract_archive
#Create a color background theme for the window
sg.theme("DarkPurple")

#Create Label, Input & Button Widgets for the 1st row
label1 = sg.Text("Select Archive:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

#Create Label, Input & Button Widgets for the 2nd row
label2 = sg.Text("Select dest dir:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

#Create Label & Button Widgets for the last row
extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

#Create the window instance with the Tile and Layout
window = sg.Window("Archive Extractor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    #1st print event and values to test read output
    print(event, values)
    #Create the archive path and the dest dir as variables
    archivepath = values["archive"]
    dest_dir = values["folder"]
    #Use the extract_archive function to call the archive & dest dir variables
    extract_archive(archivepath, dest_dir)
    #Specify the output_label key to print message once successful.
    window["output"].update(value="Extraction completed.")

window.close()