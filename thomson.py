from tkinter import *
from tkinter import ttk

thomson = Tk()

thom_p = ttk.Frame(thomson, padding=50)
thom_p.grid()
ttk.Label(thom_p, text="Thomson Page").grid(column=0, row=0)
ttk.Button(thom_p, text="Quit", command=thomson.destroy).grid(column=1, row=0)