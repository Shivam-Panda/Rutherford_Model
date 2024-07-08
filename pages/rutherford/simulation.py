from tkinter import *
from tkinter import ttk

def rutherford_simulation_render():
    page = Tk()

    home = ttk.Frame(page, padding=50)
    home.grid()
    ttk.Label(home, text="Rutherford Simulation Page").grid(column=0, row=0)

    page.mainloop()

if __name__ == '__main__':
    rutherford_simulation_render()