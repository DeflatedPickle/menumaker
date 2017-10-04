#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

import tkinter as tk

__title__ = "Constructor"
__version__ = "1.3.0"
__author__ = "DeflatedPickle"


def constructor(parent: tk.Menu, menus: dict, title: bool=True, auto_functions: bool=True):
    for menu in menus["menus"]:
        # print("Menu:", menu)
        tkmenu = tk.Menu(parent)
        for item in menus["menus"][menu]:
            # print("Item:", item)
            for command in menus["menus"][menu]["items"]:
                # print("Command:", command)
                tkmenu.add_command(label=command if not title else command.title(),
                                   command=_set_command(command) if auto_functions else None)

        # print("-----")
        parent.add_cascade(label=menu if not title else menu.title(), menu=tkmenu)


def _set_command(command):
    try:
        return getattr(__import__(__name__), command)

    except AttributeError:
        return None


if __name__ == "__main__":
    def new():
        print("New!")

    root = tk.Tk()
    menu = tk.Menu(root)

    constructor(menu, {"menus": {
        "file": {"items": ["new", "open", "save"]},
        "edit": {"items": ["undo", "redo"]}
    }})

    root.configure(menu=menu)
    root.mainloop()
