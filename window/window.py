from tkinter import *;

window=Tk() # innitialize the main window
window.title("My Application") # set the title of the window
window.geometry("400x550") # set the size of the window
window.configure(bg="lightblue") # set the background color of the window

icon= PhotoImage(file="logo.png") # load an icon image
window.iconphoto(True, icon) # set the window icon


window.mainloop()