from tkinter import *

def print_text():
    print(text_area.get("1.0", END)) # "1.0" means line 1, character 0 (the very beginning of the text area) and END means the end of the text area. This will print all the text in the text area.

window = Tk()

text_area = Text(window,
                 bg="light yellow",
                 fg="Black",
                 padx=10,pady=10,
                 height=8,width=20,
                 font=("Ink Free", 20)) # Dont use .pack() here to avoid NoneType assignment->as it returns None
text_area.insert(END, "Welcome to Ankan's World") # placeHolder text
text_area.pack()

button = Button(window,
                text="Click Me",
                bg="blue",
                command=print_text)
button.pack()

window.mainloop()
