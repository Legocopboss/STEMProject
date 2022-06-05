from tkinter import *

from database import *
from functionLibrary import *

root = Tk()
root.geometry("400x400")
root.resizable(True, True)

first_frame = Frame(root)
first_frame.pack(expand=1, fill=BOTH)

welcome_frame = Frame(root)
welcome_frame.pack(expand=1, fill=BOTH)
error_login_frame = Frame(root)
error_login_frame.pack(expand=1, fill=BOTH)

usernameVar = StringVar()
passwordVar = StringVar()


def login():
    u = usernameVar.get()
    p = passwordVar.get()
    print(u + p)
    if u == "" or p == "":
        return

    clear_frame(first_frame)

    label = Label(welcome_frame, text=admCheckLogin(u, p)).pack()

    # if u or p == "":
    #    error_label = Label(root, text="One or more fields is incorrect.").pack()


def backToCustLogin():
    clear_frame(first_frame)
    exec(open("./customerLoginUI.py").read())


user_label = Label(first_frame, text="Enter Username:").pack()
user = Entry(first_frame, textvariable=usernameVar)
user.pack()
user.focus()
pass_label = Label(first_frame, text="Enter Password:").pack()
passW = Entry(first_frame, show="*", textvariable=passwordVar)
passW.pack()
passW.focus()

loginButton = Button(first_frame, text="Login", bg="grey", command=login).pack()

backButton = Button(first_frame, text="Back", bg="pink", command=backToCustLogin)
backButton.pack()
backButton.place(bordermode=OUTSIDE, x=0.1, y=0.1)

# command=checkLogin()

root.mainloop()
