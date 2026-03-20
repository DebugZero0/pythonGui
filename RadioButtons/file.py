from tkinter import *

option=["Option 1", "Option 2", "Option 3"]
def show():
    if x.get()!=-1:
        print("You selected:", option[x.get()])

window=Tk()

x=IntVar()
x.set(-1)  # Set to a value that doesn't correspond to any option

for i in range(len(option)):
    Radiobutton(window,
                text=option[i],
                variable=x,
                value=i,
                padx=20,
                font=("Arial", 16),
                command=show).pack(anchor=W) # anchor W means left side of the window 

window.mainloop()