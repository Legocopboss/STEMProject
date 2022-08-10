from tkinter import *

from functionLibrary import *


def ManagerUIFrame(root):
    root.title("Manager UI")

    first_frame = Frame(root)
    first_frame.pack(expand=1, fill=BOTH)
    first_frame.grid_columnconfigure(1, weight=1)

    welcome_frame = Frame(root)
    welcome_frame.pack(expand=1, fill=BOTH)
    error_login_frame = Frame(root)
    error_login_frame.pack(expand=1, fill=BOTH)

    def backToCustLogin():
        clear_frame(first_frame, True)
        from customerLoginUI import customerLogin
        customerLogin(root)

    Label(first_frame, text="Lol you have no permissions").grid(row=1, column=1)
    Label(first_frame, text="stupid manager").grid(row=2, column=1)

    Button(first_frame, text="Back To Customer Login", bg="pink", command=backToCustLogin).grid(row=0, column=0)

    # root.mainloop()


if __name__ == "__adminUI__":
    ManagerUIFrame()
