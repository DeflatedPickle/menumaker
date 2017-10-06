import tkinter as tk
from collections import OrderedDict
import menumaker

def new():
    print("New!")

root = tk.Tk()
menubar = tk.Menu(root)

var = tk.IntVar()
var2 = tk.BooleanVar()

var.trace_variable("w", lambda *args: print("Changed!"))

menumaker.constructor(menubar, OrderedDict([
    ("file", {"items": ["new", "open", "save"]}),
    ("edit", {"items": ["undo", "redo", "---", "cut", "copy", "paste"]}),
    ("-background", {"items": ["(var)green", "(var)red"]}),
    ("view", {"items": ["[var2]toolbar", "-background"]})
]))

root.configure(menu=menubar)
root.mainloop()
