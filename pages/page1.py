from tkinter import *
from tkinter import ttk

def render():
    page = Tk()

    home = ttk.Frame(page, padding=50)
    home.grid()
    ttk.Label(home, text="Second Page").grid(column=0, row=0)
    ttk.Button(home, text="Quit", command=page.destroy).grid(column=0, row=1)

    page.mainloop()

if __name__ == '__main__':
    render()