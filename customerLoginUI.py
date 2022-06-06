from tkinter import *

from database import *
from functionLibrary import *
from loginUI import LoginfirstFrame
from posUI import posUIDEF

root = Tk()
root.geometry("400x400")
root.resizable(True, True)

first_frame = Frame(root)
first_frame.pack(expand=1, fill=BOTH)

welcome_frame = Frame(root)
welcome_frame.pack(expand=1, fill=BOTH)
error_login_frame = Frame(root)
error_login_frame.pack(expand=1, fill=BOTH)


# exec(open("./database.py").read())





def login():
    idNumber = mystring.get()
    print(idNumber)
    if idNumber == "":
        return

    clear_frame(first_frame)

    def newP():
        nameStr = inputStr.get()
        print(nameStr)
        newPerson(idNumber, nameStr)
        clear_frame(error_login_frame)
        label = Label(welcome_frame,
                      text=f"Welcome {printInfo(idNumber, 2)}. You have a balance of {printInfo(idNumber, 3)} B").pack()
        Button(welcome_frame, text="Return to login", bg="pink", command=backToLogin).pack()

    inputStr = StringVar()

    print(idNumber + " is being proccessed")
    result = checkLogin(idNumber)
    print(result)
    if not result:
        error_label = Label(error_login_frame, text="You are not in our system. Lets add you!").pack()
        error_label_inst = Label(error_login_frame, text="Please Type Name (Ex: First Last): ").pack()
        input_entry = Entry(error_login_frame, textvariable=inputStr)
        input_entry.pack()
        input_entry.focus()
        ConfirmButton = Button(error_login_frame, text="Confirm", bg="grey", command=newP).pack()
    else:
        posUIDEF(idNumber)
        label = Label(welcome_frame,
                      text=f"Welcome {printInfo(idNumber, 2)}. You have a balance of {printInfo(idNumber, 3)} Bollars").pack()


def adminLogin():
    clear_frame(first_frame)
    # root.destroy()
    LoginfirstFrame()


def backToLogin():
    clear_frame(welcome_frame)
    exec(open("./customerLoginUI.py").read())
    root.destroy()


mystring = StringVar()

id_label = Label(first_frame, text="Scan ID:").pack()
id_entry = Entry(first_frame, textvariable=mystring)
id_entry.pack()
id_entry.focus()
# root.bind("<Return>", login)
loginButton = Button(first_frame, text="Login", bg="grey", command=login).pack()

adminLoginButton = Button(first_frame, text="Admin Login", bg="pink", command=adminLogin)
adminLoginButton.pack()
adminLoginButton.place(bordermode=OUTSIDE, height=30, width=90, x=-0.1, y=-0.1)
# would prefer for admin button to be botton right/left but fuck formatting

root.mainloop()
