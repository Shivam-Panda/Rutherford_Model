from tkinter import *
from tkinter import ttk

def thomson_simulation_render():
    page = Tk()

    home = ttk.Frame(page, padding=50)
    home.grid()
    ttk.Label(home, text="Thomson Simulation Page").grid(column=0, row=0)

    page.mainloop()

if __name__ == '__main__':
    thomson_simulation_render()