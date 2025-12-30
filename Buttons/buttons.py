from tkinter import *

count=0
def click():
    global count
    count += 1
    print(f"You clicked the button {count} times")



window=Tk()

photo=PhotoImage(file="Buttons/like.png") 
resize=photo.subsample(5,5) 

window.title("Button Example")
window.geometry("400x300")
window.configure(bg="lightblue")

button=Button(window,
              state="active", # normal, active, disabled
              text="click",
              command=click,
              font=("comic sans", 30),
              fg="green",
              bg="white",
              padx=40,
              activeforeground="red",# Change text color when clicked
              activebackground="black",
              image=resize,
              compound="right") # image on left of text
button.pack(side="top", pady=20)

window.mainloop()