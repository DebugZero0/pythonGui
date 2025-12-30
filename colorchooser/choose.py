from tkinter import *
from tkinter import colorchooser

window=Tk()
window.geometry("300x200")
def choose_color():
    # color=colorchooser.askcolor()
    # print(color)
    window.configure(bg=colorchooser.askcolor()[1])

button=Button(window,text="Choose Color",command=choose_color)
button.pack()

window.mainloop()