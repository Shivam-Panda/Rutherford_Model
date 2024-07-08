from tkinter import *
from tkinter import ttk

ruther = Tk()

ruther_p = ttk.Frame(ruther, padding=50)
ruther_p.grid()
ttk.Label(ruther_p, text="Rutherford Page").grid(column=0, row=0)
ttk.Button(ruther_p, text="Quit", command=ruther.destroy).grid(column=1, row=0)
