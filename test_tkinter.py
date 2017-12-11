import tkinter as tk

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
menubar = tk.Menu()

var = tk.IntVar()
var2 = tk.BooleanVar()

var.trace_variable("w", lambda *args: print("Changed!"))

file = tk.Menu(menubar)
file.add_command(label="New", command=new, accel="Ctrl+N")
root.bind("<Control-n>", new)
file.add_command(label="Open")
file.add_command(label="Save")
menubar.add_cascade(label="File", menu=file)

edit = tk.Menu(menubar)
edit.add_command(label="Undo", command=undo, accel="Ctrl+Z")
root.bind("<Control-z>", undo)
edit.add_command(label="Redo", command=redo, accel="Ctrl+Shift+Z")
root.bind("<Control-Shift-Z>", redo)
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete", command=delete, accel="Delete")
root.bind("<Delete>", delete)
edit.add_command(label="Delete All", command=delete_all, accel="Alt-Delete")
root.bind("<Alt-Delete>", delete_all)
menubar.add_cascade(label="Edit", menu=edit)

background = tk.Menu(menubar)
background.add_radiobutton(label="Green", variable=var)
background.add_radiobutton(label="Red", variable=var)

view = tk.Menu(menubar)
view.add_checkbutton(label="Toolbar", variable=var2)
view.add_cascade(label="Background", menu=background)
menubar.add_cascade(label="View", menu=view)

root.configure(menu=menubar)
root.mainloop()