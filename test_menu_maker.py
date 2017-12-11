import tkinter as tk
import menumaker

def new(*args):
    print("New!")

def undo(*args):
    print("Undo.")

def redo(*args):
    print("Redo.")

def delete(*args):
    print("Bwahm!")

def delete_all(*args):
    print("More bwahm!")

root = tk.Tk()
menubar = tk.Menu(root)

var = tk.IntVar()
var2 = tk.BooleanVar()

var.trace_variable("w", lambda *args: print("Changed!"))

menumaker.constructor(menubar, [
    ("file", {"items": ["new ~ctrl+n", "open", "save"]}),
    ("edit", {"items": ["undo ~ctrl+z", "redo ~ctrl+shift+z", "---", "cut", "copy", "paste", "delete ~delete", "delete all ~alt+delete"]}),
    ("-background", {"items": ["(var) green", "(var) red"]}),
    ("view", {"items": ["[var2] toolbar", "-background"]})
])

root.configure(menu=menubar)
root.mainloop()