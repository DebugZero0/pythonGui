from tkinter import *
from tkinter import filedialog

def openFile():
    filePath=filedialog.askopenfilename(initialdir="C:\\Users\\ANKAN\\OneDrive\\Desktop\\VS CODE\\Python\\My Gui\\FilesHandling",
                                        filetypes=(("Text File","*.txt"),("All Files","*.*")),
                                        title="Open a File")
    # file=open(filePath,'r')
    # print(file.read())
    # file.close()

    with open(filePath,'r') as f:
        print(f.read())

window=Tk()
Button(window,command=openFile,text="Open File").pack()
window.mainloop()