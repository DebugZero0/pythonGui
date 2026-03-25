from tkinter import *

root=Tk()
root.title("Practice Application")
root.geometry("800x900")

# Input from different widgets and display it in the console when a button is clicked.

label=Label(root, text="Hello World", font=("Arial", 20))
label.pack(pady=20)
Button(root, text="Click Me", font=("Arial", 15), command=lambda: print(label.cget("text"))).pack(pady=20)

entry=Entry(root, font=("Arial", 15))
entry.pack(pady=20)
Button(root, text="Submit", font=("Arial", 15), command=lambda: print(entry.get())).pack(pady=20)

text=Text(root, height=5, width=30, font=("Arial", 15))
text.pack(pady=20)
Button(root, text="Show Text", font=("Arial", 15), command=lambda: print(text.get("1.0", END))).pack(pady=20)

# checkbox and radio button
var1=IntVar()
check=Checkbutton(root, text="Accept Terms",
                  variable=var1,
                  onvalue=1, offvalue=0, 
                  font=("Arial", 15),
                  command=lambda: print("Checkbox is", "Checked" if var1.get() == 1 else "Unchecked"))
check.pack(pady=20)

var2=IntVar()
var2.set(-1) # to set default value for radio button
for i in range(3):
    Radiobutton(root,
                text=f"Option {i+1}",
                variable=var2,
                value=i,
                font=("Arial", 15),
                command=lambda: print("Selected Option:", var2.get() + 1)).pack(anchor=W)

root.mainloop()