from tkinter import *
from tkinter import ttk

root = Tk()

# def open_render():
#     root.destroy()
#     render()

home = ttk.Frame(root, padding=50)
home.grid()
ttk.Label(home, text="Home Page").grid(column=0, row=0)
# ttk.Button(home, text="Open Second", command=open_render).grid(column=0, row=1)
ttk.Button(home, text="Home Quit", command=root.destroy).grid(column=1, row=1)

root.mainloop()