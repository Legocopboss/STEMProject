from tkinter import *

from adminUI import adminUIDEF
from functionLibrary import *


def LoginfirstFrame():
    root = Tk()
    root.title("Admin Login")
    root.geometry("400x400")
    root.resizable(True, True)

    first_frame = Frame(root)
    first_frame.pack(expand=1, fill=BOTH)
    first_frame.grid_columnconfigure(1, weight=1)

    welcome_frame = Frame(root)
    welcome_frame.pack(expand=1, fill=BOTH)
    error_login_frame = Frame(root)
    error_login_frame.pack(expand=1, fill=BOTH)

    def Alogin():
        u = usernameVar.get()
        p = passwordVar.get()
        print(u + p)
        if u == "" or p == "":
            return

        clear_frame(first_frame)

        adm, man = admCheckLogin(u, p)

        if man:
            if adm:
                clear_frame(first_frame)
                adminUIDEF()
            else:
                clear_frame(first_frame)
                # exec(open("./managerUI.py").read())
        else:
            backToCustLogin()

        # if u or p == "":
        #    error_label = Label(root, text="One or more fields is incorrect.").pack()

    def backToCustLogin():
        clear_frame(first_frame)
        exec(open("./customerLoginUI.py").read())

    usernameVar = StringVar(root)
    passwordVar = StringVar(root)
    Label(first_frame, text="Enter Username:").grid(row=1, column=1)
    Entry(first_frame, textvariable=usernameVar).grid(row=2, column=1)
    Label(first_frame, text="Enter Password:").grid(row=3, column=1)
    Entry(first_frame, show="*", textvariable=passwordVar).grid(row=4, column=1)

    Button(first_frame, text="Login", bg="grey", command=Alogin).grid(row=5, column=1)

    Button(first_frame, text="Back To Customer Login", bg="pink", command=backToCustLogin).grid(row=0, column=0)

    Button(first_frame, text="This is probably not secure", bg="blue", command=adminUIDEF).grid(row=7, column=0)

    root.mainloop()


if __name__ == "__customerLoginUI__":
    LoginfirstFrame()
# command=checkLogin()
