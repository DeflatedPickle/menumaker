#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from collections import OrderedDict

__title__ = "Constructor"
__version__ = "1.10.2"
__author__ = "DeflatedPickle"


def constructor(parent: tk.Menu, menus: dict, title: bool=True, auto_functions: bool=True):
    all_menus = {}

    for menu in menus:
        # print("Menu:", menu)
        tkmenu = tk.Menu(parent)
        all_menus[menu] = tkmenu
        for item in menus[menu]:
            # print("Item:", item)
            for command in menus[menu]["items"]:
                # print("Command:", command)
                title = command if not title else command.title()
                if command == "---":
                    tkmenu.add_separator()

                elif "[" in command and "]" in command:
                    tkmenu.add_checkbutton(label=_remove_brackets(title, "[]"),
                                           variable=_check_brackets(command, "[]"))

                elif "(" in command and ")" in command:
                    tkmenu.add_radiobutton(label=_remove_brackets(title, "()"),
                                           variable=_check_brackets(command, "()"))

                elif "-" in command:
                    tkmenu.add_cascade(label=title.replace("-", ""), menu=all_menus[command])

                else:
                    tkmenu.add_command(label=title,
                                       command=_set_command(command) if auto_functions else None)

        # print("-----")
        if "-" not in menu:
            parent.add_cascade(label=menu if not title else menu.title(), menu=tkmenu)


def _set_command(command):
    try:
        return getattr(__import__("__main__"), command)

    except AttributeError:
        return None


def _check_variable(string: str, brackets: str):
    return string[string.index(brackets[0]) + 1:string.index(brackets[1])]


def _remove_brackets(string: str, brackets: str):
    return string[string.index(brackets[1]) + 1:]


def _check_brackets(string: str, brackets: str):
    if not string.index(brackets[0]) == string.index(brackets[1]) + 1:
        return getattr(__import__("__main__"), _check_variable(string, brackets))

    else:
        return None


if __name__ == "__main__":
    def new():
        print("New!")

    root = tk.Tk()
    menu = tk.Menu(root)

    var = tk.IntVar()
    var2 = tk.BooleanVar()

    var.trace_variable("w", lambda *args: print("Changed!"))

    constructor(menu, OrderedDict([
        ("file", {"items": ["new", "open", "save"]}),
        ("edit", {"items": ["undo", "redo", "---", "cut", "copy", "paste"]}),
        ("-background", {"items": ["(var)green", "(var)red"]}),
        ("view", {"items": ["[var2]toolbar", "-background"]})
    ]))

    root.configure(menu=menu)
    root.mainloop()
