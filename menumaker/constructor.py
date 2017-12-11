#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""""""

from __future__ import absolute_import, division, print_function, unicode_literals

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from collections import OrderedDict

__title__ = "Constructor"
__version__ = "1.13.8"
__author__ = "DeflatedPickle"


# def constructor(parent: tk.Menu, menus: dict, title: bool=True, auto_functions: bool=True):
def constructor(parent, menus, title=True, auto_functions=True, auto_bind=True, add_bind=True):
    menus = OrderedDict(menus)
    all_menus = {}

    for menu in menus:
        # print("Menu:", menu)
        tkmenu = tk.Menu(parent)
        all_menus[menu] = tkmenu
        for item in menus[menu]:
            # print("Item:", item)
            for command in menus[menu]["items"]:
                # print("Command:", command)
                title = _remove_image(_remove_accel(command if not title else command.title().lstrip()))

                if auto_bind:
                    if "~" in command:
                        parent.master.bind(_parse_accel_bind(command.split("~")[1]), _set_command(title.lower()), "+" if add_bind else "")

                if command == "---":
                    tkmenu.add_separator()

                elif "[" in command and "]" in command:
                    tkmenu.add_checkbutton(label=_remove_brackets(title, "[]"),
                                           variable=_check_brackets(command, "[]"),
                                           accel=_get_accel(command))

                elif "(" in command and ")" in command:
                    tkmenu.add_radiobutton(label=_remove_brackets(title, "()"),
                                           variable=_check_brackets(command, "()"),
                                           accel=_get_accel(command))

                elif "-" in command:
                    tkmenu.add_cascade(label=title.replace("-", ""), menu=all_menus[command])

                else:
                    tkmenu.add_command(label=title,
                                       command=_set_command(title.lower().replace(" ", "_")) if auto_functions else None,
                                       image=_get_image(command),
                                       accel=_get_accel(command.title()))

        # print("-----")
        if "-" not in menu:
            parent.add_cascade(label=menu if not title else menu.title(), menu=tkmenu)


def _set_command(command):
    try:
        return getattr(__import__("__main__"), command)

    except AttributeError:
        return None


def _parse_accel_bind(sequence):
    sequence = sequence.lower().split("+")
    # print("Original:", sequence)

    parse = []

    for item in sequence:
        if item == "ctrl":
            parse.append("Control")

        else:
            if len(item) > 1 or sequence[sequence.index(item) - 1] == "shift":
                item = item.title()

            parse.append(item)
        # print("Parse:", parse)

    # parse.append(sequence[-1].lower())

    join = "-".join(parse)
    # print("Join:", join)
    finished = "<" + (join if len(sequence) > 1 else join.title()) + ">"

    # print("Finished:", finished)
    return finished


def _remove_image(string):
    return string.split("|")[-1].lstrip()


def _get_image(string):
    if "|" in string:
        split = string.split("|")[0].rstrip()

    else:
        split = None

    return split


def _remove_accel(string):
    return string.split("~")[0].rstrip()


def _get_accel(string):
    try:
        split = string.split("~")[1]
    except IndexError:
        split = None

    return split


def _check_variable(string, brackets):
    return string[string.index(brackets[0]) + 1:string.index(brackets[1])]


def _remove_brackets(string, brackets):
    return string[string.index(brackets[1]) + 1:].lstrip()


def _check_brackets(string, brackets):
    if not string.index(brackets[0]) == string.index(brackets[1]) + 1:
        return getattr(__import__("__main__"), _check_variable(string, brackets))

    else:
        return None


if __name__ == "__main__":
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
    menu = tk.Menu(root)

    image = tk.PhotoImage("scissors", file="image.png")

    var = tk.IntVar()
    var2 = tk.BooleanVar()

    var.trace_variable("w", lambda *args: print("Changed!"))

    constructor(menu, [
        ("file", {"items": ["new ~ctrl+n", "open", "save"]}),
        ("edit", {"items": ["undo ~ctrl+z", "redo ~ctrl+shift+z", "---", "scissors| cut", "copy", "paste", "delete ~delete", "delete all ~alt+delete"]}),
        ("-background", {"items": ["(var) green", "(var) red"]}),
        ("view", {"items": ["[var2] toolbar", "-background"]})
    ])

    root.configure(menu=menu)
    root.mainloop()
