from tkinter import *

#Entery Widget = text box to enter a single line of text from user

window=Tk()
window.title("Entry Widget")
window.config(bg="black")


entry=Entry(window,font=("Arial", 14),
            bg="light blue",fg="blue",
            borderwidth=1,foreground="green") #show/hide text with show="*"
entry.pack()
entry.insert(0,"Enter your password: ")

submit_button=Button(window,text="Submit",command=lambda:print(entry.get()))
submit_button.pack(side=RIGHT) 

delete_button=Button(window,text="Delete",command=lambda:entry.delete(0,END))
delete_button.pack(side=RIGHT)
 
backspace_button=Button(window,text="Backspace",command=lambda:entry.delete(len(entry.get())-1,END))
backspace_button.pack(side=RIGHT)



window.mainloop()