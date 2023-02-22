import os
import subprocess
import time
import webbrowser
from tkinter import *
from tkinter import filedialog

from win10toast import ToastNotifier

from screenSize import ScreenSize


# building the Tkinter window
root = Tk()
root.title("Py to Exe")
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
appGeometry = ScreenSize(screenWidth, screenHeight)
root.geometry(appGeometry)
root.configure(bg="Black")

# checkbox variables
onefileCheckbuttonVar = IntVar()
windowedCheckButtonVar = IntVar()
iconCheckButtonVar = IntVar()

# opening the selected file
def selectFile():
    filetypes = (
        ("Python Scripts", "*.py"),
        ("Icon Files", "*.ico"),
        ("All files", "*.*"),
    )

    global selectedFilename

    selectedFilename = filedialog.askopenfilename(
        title="Open files",
        filetypes=filetypes,
        initialdir="C:/Desktop",
    )
    filenameLabel.config(text=selectedFilename)
    updateCommand()


# opening the selected icon
def selectIcon():
    filetypes = (
        ("Icon Files", "*.ico"),
        ("Python Scripts", "*.py"),
        ("All files", "*.*"),
    )

    global selectedIcon

    selectedIcon = filedialog.askopenfilename(
        title="Open files",
        filetypes=filetypes,
        initialdir="C:/Desktop",
    )
    iconnameLabel.config(text=selectedIcon)
    updateCommand()


# updating the command visualiser
def updateCommand():
    global command
    global onefileCheckbuttonVarInput
    global windowedCheckButtonVarInput
    global iconCheckButtonVar
    global selectedFilename
    global selectedIcon
    command = "pyinstaller"
    onefile = " --onefile"
    windowed = " -w"

    onefileCheckbuttonVarInput = onefileCheckbuttonVar.get()
    windowedCheckButtonVarInput = windowedCheckButtonVar.get()

    iconCheckButtonVarInput = iconCheckButtonVar.get()

    if onefileCheckbuttonVarInput == 1 and windowedCheckButtonVarInput == 1:
        command = command + onefile + windowed
        print(command)
    elif onefileCheckbuttonVarInput == 1 and windowedCheckButtonVarInput == 0:
        command = command + onefile
        print(command)
    elif onefileCheckbuttonVarInput == 0 and windowedCheckButtonVarInput == 1:
        command = command + windowed
        print(command)
    else:
        command = command.replace(onefile, "")
        command = command.replace(windowed, "")

    if iconCheckButtonVarInput == 1:
        command = command + " -i " + '"' + selectedIcon + '"'
    else:
        command

    if selectedFilename != "":
        command = command + " " + '"' + selectedFilename + '"'
    else:
        command

    compileCommand.config(text=command)


# will run the command that is shown in the visualiser
def Compile():
    print(command)
    os.system(command)


openFileButton = Button(
    root,
    text="open files",
    command=selectFile,
)
openFileButton.grid(
    column=0,
    row=0,
)

filenameLabel = Label(
    root,
    text="file not selected yet!",
)
filenameLabel.grid(
    column=1,
    row=0,
)

openIconButton = Button(
    root,
    text="Select Icon",
    command=selectIcon,
)
openIconButton.grid(
    column=0,
    row=1,
)

iconnameLabel = Label(
    root,
    text="icon not selected yet!",
)
iconnameLabel.grid(
    column=1,
    row=1,
)

iconCheckButton = Checkbutton(
    root,
    text="Use Selected Icon",
    variable=iconCheckButtonVar,
    onvalue=1,
    offvalue=0,
    width=10,
    height=1,
    command=updateCommand,
)
iconCheckButton.grid(
    column=3,
    row=1,
)


onefileCheckbutton = Checkbutton(
    root,
    text="One File",
    variable=onefileCheckbuttonVar,
    onvalue=1,
    offvalue=0,
    width=10,
    height=1,
    command=updateCommand,
)
onefileCheckbutton.grid(
    column=0,
    row=2,
)

windowedCheckButton = Checkbutton(
    root,
    text="No Window",
    variable=windowedCheckButtonVar,
    onvalue=1,
    offvalue=0,
    width=10,
    height=1,
    command=updateCommand,
)
windowedCheckButton.grid(
    column=0,
    row=4,
)

compileButton = Button(
    root,
    text="Complie",
    command=Compile,
)
compileButton.grid(
    column=0,
    row=5,
)


compileCommand = Label(
    root,
    text="No command yet :)",
)
compileCommand.grid(
    column=1,
    row=5,
)

root.mainloop()
