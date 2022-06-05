from tkinter import *

root = Tk()
root.geometry("400x400")


def run():
    NONE


def login():
    u = user.get()
    p = passWord.get()

    display_label = Label(root, text="User: " + u + " Pass: " + p).pack()

    # if u or p == "":
    #    error_label = Label(root, text="One or more fields is incorrect.").pack()


user_label = Label(root, text="Enter Username:").pack()
user = Entry(root).pack()
pass_label = Label(root, text="Enter Password:").pack()
passWord = Entry(root, show="*").pack()

loginButton = Button(root, text="Login", bg="grey", command=login).pack()

# command=checkLogin()

root.mainloop()
