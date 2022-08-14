from tkinter import *

from profanity_check import predict

from functionLibrary import *
from loginUI import LoginfirstFrame
from posUI import posUIDEF


def customerLogin(root):
    root.title("Customer Login")
    root.geometry("400x400")

    first_frame = Frame(root, bg="red")
    first_frame.pack(expand=1, fill=BOTH)

    welcome_frame = Frame(root, bg="orange")
    welcome_frame.pack(expand=1, fill=BOTH)
    error_login_frame = Frame(root, bg="yellow")
    error_login_frame.pack(expand=1, fill=BOTH)

    # exec(open("./database.py").read())

    def login():
        idNumber = mystring.get()
        print(idNumber)
        if idNumber == "":
            return

        clear_frame(first_frame)
        clear_frame(error_login_frame)

        def newP():
            nameStr = inputStr.get()
            print(nameStr)
            if findByName(nameStr, 1):
                messagebox.showerror("User already exists", f"A user by this name ({nameStr}) already exists. Please "
                                                            f"contact an administrator to fix this issue")
                customerLogin(root)
            else:
                checkNameSpace = nameStr.replace(" ", "", 1)
                if checkNameSpace.__contains__(" ") or nameStr == "" or predict([nameStr]) == 1:
                    messagebox.showerror("Invald Name",
                                         "This name is invalid or contains foul language. Please try again")
                    customerLogin(root)
                else:
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

            if getSetting(1) == 0:
                messagebox.showerror("User not in database",
                                     f"User by ID Number of {idNumber} was not found in database. "
                                     f"Please contact an administrator to fix this issue")
                backToLogin()
            else:
                # Adds a new user to the database without admin approval. Maybe make it need an admin?

                error_label = Label(error_login_frame, text="You are not in our system. Lets add you!").pack()
                error_label_inst = Label(error_login_frame, text="Please Type Name (Ex: First Last): ").pack()
                input_entry = Entry(error_login_frame, textvariable=inputStr)
                input_entry.pack()
                input_entry.focus()
                ConfirmButton = Button(error_login_frame, text="Confirm", bg="grey", command=newP)
                ConfirmButton.pack()
                root.bind('<Return>', lambda event=None: ConfirmButton.invoke())

        else:
            root.unbind('<Return>')
            clear_frame(first_frame, True)
            clear_frame(welcome_frame, True)
            clear_frame(error_login_frame, True)
            posUIDEF(idNumber, root)

    def adminLogin():
        clear_frame(first_frame, True)
        # root.destroy()
        LoginfirstFrame(root)

    def backToLogin():
        clear_frame(welcome_frame, True)
        clear_frame(first_frame, True)
        clear_frame(error_login_frame, True)
        customerLogin(root)

    mystring = StringVar()

    id_label = Label(first_frame, text="Scan ID:").pack()
    id_entry = Entry(first_frame, textvariable=mystring)
    id_entry.pack()
    id_entry.focus()
    # root.bind("<Return>", login)
    loginButton = Button(first_frame, text="Login", bg="grey", command=login)
    loginButton.pack()
    root.bind('<Return>', lambda event=None: loginButton.invoke())

    adminLoginButton = Button(first_frame, text="Admin Login", bg="pink", command=adminLogin)
    adminLoginButton.pack()
    adminLoginButton.place(bordermode=OUTSIDE, height=30, width=90, x=-0.1, y=-0.1)
    # would prefer for admin button to be botton right/left but fuck formatting


if __name__ == "__runner__":
    customerLogin()
