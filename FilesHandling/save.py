from tkinter import *
from tkinter import filedialog

def saveFile():
    filePath=filedialog.asksaveasfilename(initialdir="D:\\Work\\VS CODE\\Python\\My Gui\\FilesHandling",
                                          defaultextension=".txt",
                                          filetypes=(("Text File","*.txt"),("All Files","*.*"),("HTML File","*.html")),
                                          title="Save a File")
    if not filePath: 
        return
    # get all text from text widget
    filetext=text.get(1.0,END)
    # get text from user input through console
    # filetext=input("Enter some text to save in file: ")  
    with open(filePath,'w') as f:
        f.write(filetext)

window=Tk()


Button(window,command=saveFile,text="Save").pack()

text=Text(window,font=("ink free",30),bg="light yellow",fg="black",height=10,width=30)
text.pack()

window.mainloop()