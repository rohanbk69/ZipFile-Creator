import FreeSimpleGUI as sg
from zipLogic import make_archive

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
add_button1 = sg.FileBrowse("Choose", key="file")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
add_button2 = sg.FolderBrowse("Choose", key="folder")

add_button3 = sg.Button("Compress")
update_label=sg.Text(key="output",text_color="green")
window = sg.Window("File Zipper", layout=[[label1, input1, add_button1], [label2, input2, add_button2], [add_button3,update_label]])

while True:
    event, value = window.read()
    print(event,value)
    filepaths = value["file"].split(";")
    folder = value["folder"]
    make_archive(filepaths,folder)
    window["output"].update(value="Compression Successful!")


window.close()
