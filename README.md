# menumaker
An easy solution for creating menus with TkInter in just a few lines.

```python
import tkinter as tk
import menumaker

root = tk.Tk()
menumaker.constructor(root, {"menu": {"open": {"type": "command", "command": "function()"}, "check": {"type": "checkbutton", "command": "other_function()"}}})
```