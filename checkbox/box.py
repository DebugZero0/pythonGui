from tkinter import *

def display():
    if x.get() == 1:
        print("You agreed to the terms and conditions")
    else:
        print("You didn't agree to the terms and conditions")


window=Tk()
window.title("Checkbox Widget")

x=IntVar() # to hold integer value for checkbox , if it was string use StringVar()

Checkbutton(window,
            text="I agree to the terms and conditions",
            font=("Arial", 20),
            bg="black",
            fg="#00FF00",
            activebackground="black",
            variable=x,
            onvalue=1,
            offvalue=0,
            command=display,
            padx="20").pack()

window.mainloop()