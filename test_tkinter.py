import tkinter as tk

root = tk.Tk()

def new():
    print("New!")

var = tk.IntVar()
var2 = tk.BooleanVar()

var.trace_variable("w", lambda *args: print("Changed!"))

menubar = tk.Menu()

file = tk.Menu(menubar)
file.add_command(label="New", command=new)
file.add_command(label="Open")
file.add_command(label="Save")
menubar.add_cascade(label="File", menu=file)

edit = tk.Menu(menubar)
edit.add_command(label="Undo")
edit.add_command(label="Redo")
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
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
