# menumaker
An easy solution for creating menus with TkInter in just a few lines.

What does this library do? It decreases the amount of lines needed to construct menus to a single line.

How? A function call with dictionaries and lists.

Why should I use this? It'll save you time.

## Conversion:
### Normal Tkinter:
```python
import tkinter as tk

menubar = tk.Menu()

file = tk.Menu(menubar)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")

edit = tk.Menu(menubar)
edit.add_command(label="Undo")
edit.add_command(label="Undo")
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
```

### MenuMaker:
```python
import tkinter as tk
import menumaker

menubar = tk.Menu()
menumaker.constructor(menubar, {"menus": {
    "file": {"items": ["new", "open", "save"]},
    "edit": {"items": ["undo", "redo", "---", "cut", "copy", "paste"]}}})
```

## Plan:
```python
import tkinter as tk
import menumaker

root = tk.Menu()
menumaker.constructor(root, {"menu": {"open": {"type": "command", "command": "function()"}, "check": {"type": "checkbutton", "command": "other_function()"}}})
```

## Current Example:
```python
import tkinter as tk
import menumaker

def new():
    print("New!")

root = tk.Tk()
menu = tk.Menu(root)

menumaker.constructor(menu, {"menus": {
    "file": {"items": ["new", "open", "save"]},
    "edit": {"items": ["undo", "redo"]}
}})

root.configure(menu=menu)
root.mainloop()
```