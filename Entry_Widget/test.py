# Extract numbers from entry widget and add them and show the result in label widget
from tkinter import *

operations=["Add","Sub","Mul","Div"]

def add_numbers():
    try:
        num1=float(fst.get())
        num2=float(snd.get())
        sum=num1+num2
        result.config(text="Result: "+str(sum))
    except ValueError:
        result.config(text="Please enter valid numbers")

def subtract_numbers():
    try:
        num1=float(fst.get())
        num2=float(snd.get())
        difference=num1-num2
        result.config(text="Result: "+str(difference))
    except ValueError:
        result.config(text="Please enter valid numbers")

def multiply_numbers():
    try:
        num1=float(fst.get())
        num2=float(snd.get())
        product=num1*num2
        result.config(text="Result: "+str(product))
    except ValueError:
        result.config(text="Please enter valid numbers")

def divide_numbers():
    try:
        num1=float(fst.get())
        num2=float(snd.get())
        if num2!=0:
            quotient=num1/num2
            result.config(text="Result: "+str(quotient))
        else:
            result.config(text="Cannot divide by zero")
    except ValueError:
        result.config(text="Please enter valid numbers")

def calculate():
    op = operation_var.get()
    
    if op == 0:
        add_numbers()
    elif op == 1:
        subtract_numbers()
    elif op == 2:
        multiply_numbers()
    elif op == 3:
        divide_numbers()
    else:
        result.config(text="Select an operation")

root=Tk()
root.title("Testing.......")
root.geometry("400x350")
root.resizable(0,0)
root.config(bg="lightblue")

Label(root,text="Enter 1st no:",font=("Arial",14),bg="lightblue").grid(row=0,column=0,padx=10,pady=10)
fst=Entry(root,font=("Arial",14),fg="black",borderwidth=1)
fst.grid(row=0,column=1,padx=10,pady=10)

Label(root,text="Enter 2nd no:",font=("Arial",14),bg="lightblue").grid(row=1,column=0,padx=10,pady=10)
snd=Entry(root,font=("Arial",14),fg="black",borderwidth=1)
snd.grid(row=1,column=1,padx=10,pady=10)

operation_var=IntVar()
operation_var.set(-1)  # Set to a value that doesn't correspond to any operation
for i in range(len(operations)):
    Radiobutton(
        root,
        text=operations[i],
        variable=operation_var,
        value=i,
        font=("Arial",14),
        bg="lightblue"
    ).grid(row=2+i, column=0, columnspan=2, sticky="w", padx=10)


Button(root, text="Submit", font=("Arial",14),
       bg="lightyellow", command=calculate).grid(row=6, column=0, padx=10, pady=10)
Button(root,text="Clear",font=("Arial",14),bg="lightyellow",command=lambda:[fst.delete(0,END),snd.delete(0,END),result.config(text="")]).grid(row=6, column=1, padx=10, pady=10)

result=Label(root,text="",font=("Arial",14),bg="lightblue")

result.grid(row=7,columnspan=2,padx=10,pady=10)


root.mainloop()