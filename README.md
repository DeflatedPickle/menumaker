# MenuMaker
An easy solution for creating menus for TkInter applications in just a few lines.

**What does this library do?**
It decreases the amount of lines needed to construct menus to a single line.

**How does it do it?**
A function call with a list of tuples or a dictionary.

**Why should I use this?**
It'll save you time.

**How do I get this?**
Open your terminal and type in `pip install menumaker`.

## Comparison:
Both of the following code snippets produce the same output, but as you'll see, the code from MenuMaker is much shorter.
### Normal Tkinter:
```python
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
edit.add_command(label="Undo", accel="Ctrl+Z")
root.bind("<Control-z>", undo)
edit.add_command(label="Redo", accel="Ctrl+Shift+Z")
root.bind("<Control-Shift-Z>", redo)
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete", accel="Delete")
root.bind("<Delete>", delete)
edit.add_command(label="Delete All", accel="Alt-Delete")
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
```

### MenuMaker:
```python
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
```

## Syntax:
- `[]` - A Checkbutton.
- `()` - A Radiobutton.
- `-` - A sub-menu.
- `---` - A Separator.
- `~` - An accelerator label.

If a function is found with the same name as a menu item, the command of that menu item will be set to the found function.

Putting the name of a variable inside of the brackets for a Radio or Checkbutton will set the variable used for the Radio or Checkbutton to the variable given.