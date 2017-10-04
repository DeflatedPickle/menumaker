# menumaker
An easy solution for creating menus with TkInter in just a few lines.

## Plan:
```python
import tkinter as tk
import menumaker

root = tk.Menu()
menumaker.constructor(root, {"menu": {"open": {"type": "command", "command": "function()"}, "check": {"type": "checkbutton", "command": "other_function()"}}})
```