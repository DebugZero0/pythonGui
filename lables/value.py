from tkinter import *

key=["1","2","3","4","5","6","7","8","9","0","c","="]

root=Tk()
root.geometry("200x320")
root.title("Label")
root.config(bg="lightyellow")
root.resizable(0,0)

result_lable=Label(root,text="",font=("Arial",14),bg="lightyellow",fg="black")
result_lable.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

for i in range(len(key)):
    button=Button(root,text=key[i],font=("Arial",14),bg="lightgreen",fg="black",padx=10,pady=5,command=lambda x=key[i]:result_lable.config(text=result_lable.cget("text")+x))
    button.grid(row=(i//3)+1,column=(i%3),padx=10,pady=10)


root.mainloop()