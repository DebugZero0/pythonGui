from tkinter import *

# lables= an area widget that holds text and/or images within a window

window=Tk()
window.title("Labels Example")
window.geometry("300x200")
window.configure(bg="lightblue")

lable=Label(window, text="Hello world!", font=("Arial", 18, "bold"), fg="red" , bg="yellow") 
lable.pack() # Add the label to the window\

lable2=Label(window, text="This text is positioned", font=("Arial", 14), fg="blue" , bg="lightgrey")
lable2.place(x=0, y=50) # Position the label at specific coordinates 

lable3=Label(window,
            text="This text is at the bottom",
            font=("Arial", 12),
            fg="green" ,
            bg="white",
            relief="sunken",
            bd=2,
            padx=10,
            pady=5)
lable3.pack(side="bottom") # Position the label at the bottom of the window

photo=PhotoImage(file="lables/logo.png") # Load an image file
resized_pic=photo.subsample(4,4) # Resize the image if needed 4 times smaller width and height

lable4=Label(window,
            text="Label with Image",
            font=("Arial", 12),
            fg="black" ,
            bg="white",
            image=resized_pic, 
            compound="bottom") # compound to position text relative to image
lable4.pack(side="right")




window.mainloop()