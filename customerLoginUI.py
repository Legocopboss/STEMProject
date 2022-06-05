import unittest
from tkinter import *

from database import *

# def run():
root = Tk()
root.geometry("400x400")

first_frame = Frame(root)
first_frame.pack()
welcome_frame = Frame(root)
welcome_frame.pack()
error_login_frame = Frame(root)
error_login_frame.pack()

exec(open("./database.py").read())


def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()


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
        label = Label(welcome_frame,
                      text=f"Welcome {printInfo(idNumber, 2)}. You have a balance of {printInfo(idNumber, 3)} Bollars").pack()


def checkNull():
    with unittest.TestCase.assertRaises(EXCEPTION):
        mystring.get()


mystring = StringVar()

id_label = Label(first_frame, text="Scan ID:").pack()
id_entry = Entry(first_frame, textvariable=mystring)
id_entry.pack()
id_entry.focus()
# root.bind("<Return>", login)
loginButton = Button(first_frame, text="Login", bg="grey", command=login).pack()

root.mainloop()
