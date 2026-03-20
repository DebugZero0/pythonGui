from tkinter import *;

def display():
    if x.get() == 1:
        print("You agreed to the terms and conditions")
    else:
        print("You didn't agree to the terms and conditions")

option=["Apple", "Banana", "Cherry"]
def show():
    if ch.get()!= -1:
        print(option[ch.get()])

window=Tk()

window.title("Practice Application")
window.geometry("500x400")
menubar=Menu(window)
window.config(menu=menubar, bg="#5f2790")

icon=PhotoImage(file="x_/ankan.png")
window.iconphoto(True, icon)

fileMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label='open',command=lambda:print("Opened File"))
fileMenu.add_command(label='save',command=lambda:print("Saved File"))
fileMenu.add_separator()
fileMenu.add_command(label='exit',command=window.quit)

editMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="cut",command=lambda:print("cutting..."))
editMenu.add_command(label="copy",command=lambda:print("copying..."))
editMenu.add_command(label="paste",command=lambda:print("pasting..."))
editMenu.add_separator()
editMenu.add_cascade(label="Find",command=lambda:print("Finding..."))


text_area=Text(window,
               height=5,width=30,
               bg="white",
               fg="black",
               font=("Arial", 15),
               padx=20,pady=20)
text_area.pack(side="top", padx=20, pady=20)

ch=IntVar()
ch.set(-1)
for i in range(len(option)):
    Radiobutton(window,
                bg="#5f2790",
                pady=5,
                font=("Arial", 15),
                text=option[i],
                variable=ch,
                value=i,
                activebackground="#5f2790",
                activeforeground="black",
                command=show).pack(anchor=W)

x=IntVar() # to hold integer value for checkbox , if it was string use StringVar()
Checkbutton(window,
            text="I agree to the terms and conditions",
            font=("Arial", 15),
            bg="#5f2790",
            fg="black",
            activebackground="#5f2790",
            activeforeground="black",
            variable=x,
            onvalue=1,
            offvalue=0,
            command=display,
            padx=20).pack(side="left")

pic=PhotoImage(file="x_/ankan.png")
resized_pic=pic.subsample(4,4)

lable=Label(window,
            image=resized_pic,
            bg="#5f2790")
lable.place(x=350,y=250)

submit_btn=Button(window,
                  text="Submit",
                  bg="#4CAF50",
                  fg="white",
                  font=("Arial", 15),
                  activebackground="#2e6c31",
                  activeforeground="white",
                  padx=10,
                  command=lambda: print(text_area.get("1.0", END)))
submit_btn.pack(side="bottom", pady=20)


window.mainloop()

