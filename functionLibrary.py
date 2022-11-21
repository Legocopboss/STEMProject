from tkinter import messagebox

from database import *


def clear_frame(frame, forget=False, root=None):
    # frame.configure(height=frame["height"])
    for widgets in frame.winfo_children():
        widgets.destroy()
    if root is not None:
        root.geometry("")
    if forget:
        frame.pack_forget()


def clear_root(root):
    for widgets in root.winfo_children():
        widgets.destroy()


def check_if_int(number):
    if number.isdigit():
        return True
    return False


def check_if_float(number):
    try:
        float(number)
        return True
    except:
        return False


def validateID(idnumber, root):
    if printInfo(idnumber, 1) != "Error":
        return True
    else:
        root.bell()
        messagebox.showerror("ID ERROR", f"The ID number, {idnumber}, is invalid")
        return False


def fillGrid(frame, start, end):
    while start != end:
        frame.grid_columnconfigure(start, weight=1)
        frame.grid_rowconfigure(start, weight=1)
        start = start + 1
