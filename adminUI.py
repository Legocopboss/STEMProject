from tkinter import *

# from posUI import *
from database import *
from functionLibrary import *


def adminUIDEF():
    root = Tk()
    root.geometry("400x400")
    root.resizable(True, True)

    first_frame = Frame(root)
    first_frame.pack(expand=1, fill=BOTH)
    list_users_frame = Frame(root)
    list_users_frame.pack(expand=1, fill=BOTH)

    '''
    def runButton(iN, cA):
        newButton(iN, cA)
    
    
    def remButton(iN):
        remButton(iN)
    '''

    def back():
        clear_frame(list_users_frame)
        firstFrame()

    def titleLabel(tf):
        if tf:
            Label(list_users_frame, text="Name", font='Helvetica 10 bold').grid(row=1, column=1)
            Label(list_users_frame, text="Username", font='Helvetica 10 bold').grid(row=1, column=2)
            Label(list_users_frame, text="Password", font='Helvetica 10 bold').grid(row=1, column=3)
            Label(list_users_frame, text="Admin", font='Helvetica 10 bold').grid(row=1, column=4)
            Label(list_users_frame, text="Manager", font='Helvetica 10 bold').grid(row=1, column=5)
        else:
            Label(list_users_frame, text="ID", font='Helvetica 10 bold').grid(row=1, column=1)
            Label(list_users_frame, text="Name", font='Helvetica 10 bold').grid(row=1, column=2)
            Label(list_users_frame, text="Balance", font='Helvetica 10 bold').grid(row=1, column=3)

    def accList():
        print("Accs List")
        clear_frame(first_frame)
        x = 2
        titleLabel(False)
        for r in viewTable(False):
            Label(list_users_frame, text=r[0]).grid(row=x, column=1)
            Label(list_users_frame, text=r[1]).grid(row=x, column=2)
            Label(list_users_frame, text=r[2]).grid(row=x, column=3)
            x = x + 1
        Button(list_users_frame, text="Back", bg="pink", command=back).grid(row=x + 1, column=1)

    def admList():
        print("Adm List")
        clear_frame(first_frame)
        x = 2
        titleLabel(True)
        for r in viewTable(True):
            Label(list_users_frame, text=r[0]).grid(row=x, column=1)
            Label(list_users_frame, text=r[1]).grid(row=x, column=2)
            Label(list_users_frame, text=r[2]).grid(row=x, column=3)
            Label(list_users_frame, text=r[3]).grid(row=x, column=4)
            Label(list_users_frame, text=r[4]).grid(row=x, column=5)
            x = x + 1
        Button(list_users_frame, text="Back", bg="pink", command=back).grid(row=x + 1, column=1)

    def removeUser():
        def deleteUserRun():
            print("deleting users")
            text = deleteUser(idRemVar.get())
            clear_frame(list_users_frame)
            accList()
            Label(list_users_frame, text=text).grid(row=0, column=1)

        accList()
        idRemVar = StringVar()
        Label(list_users_frame, text="ID's for removal (separate with ,): ").grid(row=0, column=1)
        idRemEntry = Entry(list_users_frame, textvariable=idRemVar).grid(row=0, column=2)
        Button(list_users_frame, text="Submit", bg="grey", command=deleteUserRun).grid(row=0, column=3)

    def toManager():
        clear_frame(first_frame)
        # exec(open("./managerUI.py").read())

    def backToCustLogin():
        clear_frame(first_frame)
        exec(open("./customerLoginUI.py").read())

    def firstFrame():
        AdminListButton = Button(first_frame, text="Admin List", command=admList).pack()
        AccsListButton = Button(first_frame, text="Accs List", command=accList).pack()
        RemoveUserButton = Button(first_frame, text="Remove User", command=removeUser).pack()
        RemoveAdmButton = Button(first_frame, text="Remove Admin/Manager", command=None).pack()  # THIS NEEDS DONE

        toManagerButton = Button(first_frame, text="To Manager UI", command=toManager).pack()
        backButton = Button(first_frame, text="Back To Customer Login", bg="pink", command=backToCustLogin)
        backButton.pack()
        backButton.place(bordermode=OUTSIDE, x=0.1, y=0.1)

    firstFrame()

    root.mainloop()


if __name__ == "__loginUI__":
    adminUIDEF()

'''
itemName = StringVar()
itemCharge = StringVar()


itemNameEntry = Entry(first_frame, text="Item Name: ").grid(row=1, column=1)
itemChargeEntry = Entry(first_frame, text="Item price: ").grid(row=1, column=2)
addButton = Button(first_frame, text="Add Item", command=runButton(itemName.get(), itemCharge.get())).grid(row=2, column=1)
deleteButton = Button(first_frame, text="Remove Item", command=remButton(itemName.get())).grid(row=2, column=2)

itemNameEntry.pack()
itemChargeEntry.pack()
addButton.pack()
deleteButton.pack()
'''

# formLabel = Label(first_frame, text="One of the fields above is not filled out.", state=DISABLED).pack()

'''
if (itemName != "" and itemCharge != ""):
    addButton['state'] = NORMAL
elif (itemName == "" or itemCharge == ""):
    formLabel['state'] = NORMAL
'''
