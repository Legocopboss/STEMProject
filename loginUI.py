from tkinter import *

from adminUI import adminUIDEF
from customerLoginUI import customerLogin
from functionLibrary import *
from managerUI import ManagerUIFrame


def LoginfirstFrame(root):
    clear_root(root)

    root.title("Admin Login")

    first_frame = Frame(root, bg="green")
    first_frame.pack(expand=1, fill=BOTH, side=TOP)
    # first_frame.grid_columnconfigure(1, weight=1)

    error_login_frame = Frame(root, bg="blue")
    error_login_frame.pack(expand=1, fill=BOTH)

    def Alogin():
        u = usernameVar.get()
        p = passwordVar.get()
        print(u + p)
        if u == "" or p == "":
            return

        clear_frame(first_frame)

        adm, man = admCheckLogin(u, p)
        print(adm + man)
        if man:
            if adm:
                clear_frame(first_frame)
                adminUIDEF(root)
            else:
                clear_frame(first_frame)
                ManagerUIFrame(root)
                # exec(open("./managerUI.py").read())
        else:
            backToCustLogin()

        # if u or p == "":
        #    error_label = Label(root, text="One or more fields is incorrect.").pack()

    def backToCustLogin():
        clear_frame(first_frame)
        customerLogin(root)

    def gogogo():
        clear_frame(first_frame)
        adminUIDEF(root)

    usernameVar = StringVar(root)
    passwordVar = StringVar(root)
    Label(first_frame, text="Enter Username:").grid(row=1, column=1)
    Entry(first_frame, textvariable=usernameVar).grid(row=2, column=1)
    Label(first_frame, text="Enter Password:").grid(row=3, column=1)
    Entry(first_frame, show="*", textvariable=passwordVar).grid(row=4, column=1)

    Button(first_frame, text="Login", bg="grey", command=Alogin).grid(row=5, column=1)

    Button(first_frame, text="Back To Customer Login", bg="pink", command=backToCustLogin).grid(row=0, column=0)

    Button(first_frame, text="This is probably not secure", bg="blue", command=gogogo).grid(row=7, column=0)

    #root.mainloop()


if __name__ == "__customerLoginUI__":
    LoginfirstFrame()
# command=checkLogin()
