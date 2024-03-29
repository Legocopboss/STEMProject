from tkinter import *

from adminUI import adminUIDEF
from functionLibrary import *
from managerUI import ManagerUIFrame


def LoginfirstFrame(root):
    clear_root(root)

    root.title("Admin Login")

    first_frame = Frame(root, bg="grey")
    first_frame.pack(expand=1, fill=BOTH, side=TOP)
    # first_frame.grid_columnconfigure(1, weight=1)

    error_login_frame = Frame(root, bg="white")
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
                clear_frame(first_frame, True)
                adminUIDEF(root, u)
            else:
                clear_frame(first_frame, True)
                ManagerUIFrame(root, u)
        else:
            messagebox.showerror("Login Denied", "Incorrect Username or Password")
            backToCustLogin()

        # if u or p == "":
        #    error_label = Label(root, text="One or more fields is incorrect.").pack()

    def backToCustLogin():
        clear_frame(first_frame)
        from customerLoginUI import customerLogin
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

    loginBut = Button(first_frame, text="Login", bg="cyan", command=Alogin)
    loginBut.grid(row=5, column=1)
    root.bind('<Return>', lambda event=None: loginBut.invoke())

    Button(first_frame, text="Back To Customer Login", bg="cyan", command=backToCustLogin).grid(row=0, column=0)

    if getSetting(2):
        Button(first_frame, text="This is probably not secure", bg="cyan", command=gogogo).grid(row=7, column=0)

    # root.mainloop()


if __name__ == "__customerLoginUI__":
    LoginfirstFrame()
# command=checkLogin()
