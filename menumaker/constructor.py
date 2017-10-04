#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk

__title__ = "Constructor"
__version__ = "1.1.0"
__author__ = "DeflatedPickle"


def constructor(parent: tk.Menu, menus: dict, title: bool=True):
    for menu in menus["menus"]:
        # print("Menu:", menu)
        tkmenu = tk.Menu(parent)
        for item in menus["menus"][menu]:
            # print("Item:", item)
            tkmenu.add_command(label=item if not title else item.title())

        parent.add_cascade(label=menu if not title else menu.title(), menu=tkmenu)
        # print("-----")


if __name__ == "__main__":

    root = tk.Tk()
    menu = tk.Menu(root)

    constructor(menu, {"menus": {
        "file": ["new", "open", "save"],
        "edit": ["undo", "redo"]
    }})

    root.configure(menu=menu)
    root.mainloop()
