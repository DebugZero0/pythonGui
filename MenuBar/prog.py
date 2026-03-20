from tkinter import *

def openFile():
    print("Open File Dialog Box")
def saveFile():
    print("Save File Dialog Box")

window=Tk()
menubar=Menu(window) # To create menu bar
window.config(menu=menubar) # To display menu bar at the top of the window , menu is the option which is used to display menu bar in the window

filemenu=Menu(menubar,tearoff=0) # To create menu in the menu bar , tearoff=0 is used to remove dashed line at the top of the menu
menubar.add_cascade(label="File",menu=filemenu) # To add menu in the menu bar , label is the name of the menu and menu is the menu object which we want to add in the menu bar
filemenu.add_command(label="Open",command=openFile) # To add command in the menu , label is the name of the command and command is the function which we want to execute when we click on the command
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=window.quit)


editmenu=Menu(menubar,tearoff=0) # To create edit menu , tearoff=0 is used to remove dashed line at the top of the menu
menubar.add_cascade(label="Edit",menu=editmenu) 
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_separator()
editmenu.add_command(label="Find")

window.mainloop()