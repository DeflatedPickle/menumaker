# MenuMaker
An easy solution for creating menus for TkInter applications in just a few lines.

**What does this library do?**
It decreases the amount of lines needed to construct menus to a single line.

**How does it do it?**
A function call with a list of tuples or a dictionary.

**Why should I use this?**
It'll save you time.

## Comparison:
Both of the following code snippets produce the same output, but as you'll see, the code from MenuMaker is much shorter.
### Normal Tkinter:
```python
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
```

### MenuMaker:
```python
import tkinter as tk
import menumaker

def new():
    print("New!")

root = tk.Tk()
menubar = tk.Menu(root)

var = tk.IntVar()
var2 = tk.BooleanVar()

var.trace_variable("w", lambda *args: print("Changed!"))

menumaker.constructor(menubar, [
    ("file", {"items": ["new", "open", "save"]}),
    ("edit", {"items": ["undo", "redo", "---", "cut", "copy", "paste"]}),
    ("-background", {"items": ["(var)green", "(var)red"]}),
    ("view", {"items": ["[var2]toolbar", "-background"]})
])

root.configure(menu=menubar)
root.mainloop()
```

## Syntax:
- `[]` - A Checkbutton.
- `()` - A Radiobutton.
- `-` - A sub-menu.
- `---` - Separator.

If a function is found with the same name as a menu item, the command of that menu item will be set to the found function.

Putting the name of a variable inside of the brackets for a Radio or Checkbutton will set the variable used for the Radio or Checkbutton to the variable given.