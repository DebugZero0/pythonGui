from tkinter import *

# Listbox = A listing of selectable text items within its own container
def submit():
    food=[]
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print("You have ordered: ")
    for item in food:
        print(item)

def addItems():
    listbox.insert(listbox.size()+1, entry.get()) 
    listbox.config(height=listbox.size())

def dlt():
    for index in reversed(listbox.curselection()): # reverse to avoid index shifting
        listbox.delete(index)
    listbox.config(height=listbox.size())


window=Tk()

listbox=Listbox(window,
        font=("constantia", 30),width=12,
        bg="black",fg="white",
        selectmode=MULTIPLE) #SINGLE, BROWSE, MULTIPLE, EXTENDED
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Burger")
listbox.insert(3, "Hotdog")
listbox.insert(4, "Spaghetti")
listbox.insert(5, "Pasta")

entry=Entry(window,
            font=("constantia", 15),
            bg="yellow",fg="Red")
entry.pack()

submit=Button(window,
              text="Submit",
              padx=10,pady=5,
              command=submit).pack()

add=Button(window,
           text="Add Item",
           padx=10,pady=5,
           command=addItems).pack()

delete=Button(window,
                text="Delete",
                padx=10,pady=5,
                command=dlt).pack()

listbox.config(height=listbox.size())
window.mainloop()