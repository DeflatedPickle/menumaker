#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk

__title__ = "Constructor"
__version__ = "1.0.1"
__author__ = "DeflatedPickle"


def constructor(parent: tk.Menu, menus: dict):
    for menu in menus["menu"]:
        # print("Menu:", menu)
        tkmenu = tk.Menu(parent)
        for item in menus["menu"][menu]:
            # print("Item:", item)
            tkmenu.add_command(label=item)

        parent.add_cascade(label=menu, menu=tkmenu)
        # print("-----")


if __name__ == "__main__":

    root = tk.Tk()
    menu = tk.Menu(root)

    constructor(menu, {"menu": {
        "file": ["new", "open", "save"],
        "edit": ["undo", "redo"]
    }})

    root.configure(menu=menu)
    root.mainloop()
