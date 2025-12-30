from tkinter import *

def display():
    print("Scale value is:", x.get())
window=Tk()
window.config(bg="#050E3C")
window.title("Scale Widget Example")


x = IntVar()
Scale(window,
      from_=100,
      to=0,
      length=600,
      orient=VERTICAL, # VERTICAL or HORIZONTAL
      font=("consolas", 16),
      tickinterval=10,
      showvalue=1, # 1 show the current value on the scale, 0 hide it
      variable=x,
      troughcolor="#3DB6B1", # color of the scale
      resolution=2, # step size
      fg="#DC0000",
      bg="#002455").pack()

Button(window,
       text="Submit",
       command=display).pack()











window.mainloop()