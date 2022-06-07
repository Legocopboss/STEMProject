from tkinter import *

from adminUI import adminUIDEF
from database import *
from functionLibrary import *


def LoginfirstFrame():
    root = Tk()
    root.geometry("400x400")
    root.resizable(True, True)

    first_frame = Frame(root)
    first_frame.pack(expand=1, fill=BOTH)

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
            exec(open("./customerLoginUI.py").read())

        # if u or p == "":
        #    error_label = Label(root, text="One or more fields is incorrect.").pack()

    def backToCustLogin():
        clear_frame(first_frame)
        exec(open("./customerLoginUI.py").read())

    usernameVar = StringVar(root)
    passwordVar = StringVar(root)
    user_label = Label(first_frame, text="Enter Username:").pack()
    user = Entry(first_frame, textvariable=usernameVar)
    user.pack()
    user.focus()
    pass_label = Label(first_frame, text="Enter Password:").pack()
    passW = Entry(first_frame, show="*", textvariable=passwordVar)
    passW.pack()

    loginButton = Button(first_frame, text="Login", bg="grey", command=Alogin).pack()

    backButton = Button(first_frame, text="Back To Customer Login", bg="pink", command=backToCustLogin)
    backButton.pack()
    backButton.place(bordermode=OUTSIDE, x=0.1, y=0.1)

    root.mainloop()


if __name__ == "__customerLoginUI__":
    LoginfirstFrame()
# command=checkLogin()
