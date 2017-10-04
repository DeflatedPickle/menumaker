import tkinter as tk


def constructor(parent: tk.Tk, menus: dict):
    for menu in menus["menu"]:
        print("Menu", menu)
        for item in menus["menu"][menu]:
            print("Item", item)

        print("---")


if __name__ == "__main__":

    root = tk.Tk()
    constructor(root, {"menu": {
        "file": ["new", "open", "save"],
        "edit": ["undo", "redo"]
    }})
    root.mainloop()
