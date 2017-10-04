# MenuMaker
An easy solution for creating menus with TkInter in just a few lines.

What does this library do? It decreases the amount of lines needed to construct menus to a single line.

How? A function call with dictionaries and lists.

Why should I use this? It'll save you time.

## Comparison:
### Normal Tkinter:
```python
import tkinter as tk

menubar = tk.Menu()

file = tk.Menu(menubar)
file.add_command(label="New")
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
background.add_radiobutton(label="Green")
background.add_radiobutton(label="Red")

view = tk.Menu(menubar)
view.add_checkbutton(label="Toolbar")
view.add_cascade(label="Background", menu=background)
menubar.add_cascade(label="View", menu=view)
```

### MenuMaker:
```python
import tkinter as tk
from collections import OrderedDict
import menumaker

menubar = tk.Menu()
menumaker.constructor(menubar, {"menus": OrderedDict([
    ("file", {"items": ["new", "open", "save"]}),
    ("edit", {"items": ["undo", "redo", "---", "cut", "copy", "paste"]}),
    ("-background", {"items": ["()green", "()red"]}),
    ("view", {"items": ["[]toolbar", "-background"]})
])})
```