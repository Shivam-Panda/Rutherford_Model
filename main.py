from tkinter import *
from tkinter import ttk
from thomson import thomson
from rutherford import ruther

def thom_render():
    thomson.mainloop()
    root.destroy()

def ruther_render():
    ruther.mainloop()
    root.destroy()

root = Tk()

home = ttk.Frame(root, padding=50)
home.grid()
ttk.Label(home, text="Home Page").grid(column=0, row=0)
ttk.Button(home, text="Thomson", command=thom_render).grid(column=0, row=1)
ttk.Button(home, text="Rutherford", command=ruther_render).grid(column=1, row=1)

root.mainloop()