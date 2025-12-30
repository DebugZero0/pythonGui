from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title="Info",message="This is a message box")
    # messagebox.showwarning(title="Warning",message="You have a virus!")
    # messagebox.showerror(title="Error",message="Fatal Error! System Shutdown!")

    # print(messagebox.askquestion(title="Question",message="Do you like Python?"))
    # print(messagebox.askokcancel(title="Ok Cancel",message="Do you want to proceed?"))
    # print(messagebox.askyesno(title="Yes No",message="Do you want to continue?"))
    # print(messagebox.askretrycancel(title="Retry Cancel",message="Try again later."))
    print(messagebox.askyesnocancel(title="Delete",message="Do you want to delete this file?"))


window=Tk()

Button(window,
       text="Click Me",
       command=click).pack()









window.mainloop()