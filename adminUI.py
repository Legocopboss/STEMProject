from tkinter import *
# from posUI import *
from tkinter import messagebox

from database import *
from functionLibrary import *


def adminUIDEF():
    root = Tk()
    root.geometry("400x400")
    root.resizable(True, True)

    first_frame = Frame(root)
    first_frame.pack(expand=1, fill=BOTH)
    list_frame = Frame(root)
    list_frame.pack(expand=1, fill=BOTH, side=BOTTOM)
    edit_user_frame_TOP = Frame(root)
    edit_user_frame_TOP.pack(expand=1, fill=BOTH, side=TOP)
    edit_usr_frame = Frame(root)
    edit_usr_frame.pack(expand=1, fill=BOTH)

    '''
    def runButton(iN, cA):
        newButton(iN, cA)
    
    
    def remButton(iN):
        remButton(iN)
    '''

    def back():
        clear_frame(list_frame)
        clear_frame(edit_usr_frame)
        clear_frame(edit_user_frame_TOP)
        firstFrame()

    def titleLabel(tf):
        if tf == "adm":
            Label(list_frame, text="Name", font='Helvetica 10 bold').grid(row=1, column=1)
            Label(list_frame, text="Username", font='Helvetica 10 bold').grid(row=1, column=2)
            Label(list_frame, text="Password", font='Helvetica 10 bold').grid(row=1, column=3)
            Label(list_frame, text="Admin", font='Helvetica 10 bold').grid(row=1, column=4)
            Label(list_frame, text="Manager", font='Helvetica 10 bold').grid(row=1, column=5)
        if tf == "cust":
            Label(list_frame, text="ID", font='Helvetica 10 bold').grid(row=1, column=1)
            Label(list_frame, text="Name", font='Helvetica 10 bold').grid(row=1, column=2)
            Label(list_frame, text="Balance", font='Helvetica 10 bold').grid(row=1, column=3)
        if tf == "trans":
            Label(list_frame, text="Employee User", font='Helvetica 10 bold').grid(row=1, column=1)
            Label(list_frame, text="Customer Name", font='Helvetica 10 bold').grid(row=1, column=2)
            Label(list_frame, text="Customer ID", font='Helvetica 10 bold').grid(row=1, column=3)
            Label(list_frame, text="Purchases", font='Helvetica 10 bold').grid(row=1, column=4)
            Label(list_frame, text="Total", font='Helvetica 10 bold').grid(row=1, column=5)
            Label(list_frame, text="Remaining Balance", font='Helvetica 10 bold').grid(row=1, column=6)
            Label(list_frame, text="Time of Purchase", font='Helvetica 10 bold').grid(row=1, column=7)

    def makeTable(tf):
        clear_frame(first_frame)
        titleLabel(tf)
        x = 2
        y = 1
        table = viewTable(False) if tf == "cust" else viewTable(
            True) if tf == "adm" else transactionLog() if tf == "trans" else None
        for r in viewTable(False):
            for t in r:
                Label(list_frame, text=r[y - 1]).grid(row=x, column=y)
                y += 1
            x += 1
            y = 1
        Button(list_frame, text="Back", bg="pink", command=back).grid(row=x + 1, column=1)

    def accList():
        print("Accs List")
        makeTable("cust")

    def admList():
        print("Adm List")
        makeTable("adm")

    def transLog():
        # Label(list_frame, text="Search Query: ")
        makeTable("trans")

    def editUser():
        accList()
        options = {'Edit User Balance', 'Delete User', 'Edit User Name'}
        ddVar = StringVar(root)
        ddVar.set('Edit User Balance')
        popupMenu = OptionMenu(edit_user_frame_TOP, ddVar, *options)
        Label(edit_user_frame_TOP, text="Options: ").grid(row=1, column=1)
        popupMenu.grid(row=1, column=2)

        def editUserBalance():
            print("editing balance")
            clear_frame(edit_usr_frame)

            def editBalance():
                text = newTransaction_WithDepos(idVarB.get(), int(amt.get()))
                clear_frame(edit_usr_frame)
                accList()
                Label(edit_usr_frame, text=text).grid(row=1, column=1)

            def validate():
                testAmt = amt.get()

                if False in [dg.isdigit() for dg in testAmt]:
                    editBalance()
                else:
                    None

            def amount():
                print(idVarB.get())
                if printInfo(idVarB.get(), 1) == "Error":
                    messagebox.showerror('error', "ID not valid")
                    editUserBalance()
                clear_frame(edit_usr_frame)
                accList()
                Label(edit_usr_frame,
                      text="Balance Withdrawl/Deposit Amount (withdrawl will be a negative value): ").grid(row=2,
                                                                                                           column=1)
                Entry(edit_usr_frame, textvariable=amt).grid(row=2, column=2)
                Button(edit_usr_frame, text="Submit", bg="grey", command=validate).grid(row=2, column=3)

            idVarB = StringVar()
            amt = IntVar()
            Label(edit_usr_frame, text="ID for balance edit (singular ID): ").grid(row=2, column=1)
            Entry(edit_usr_frame, textvariable=idVarB).grid(row=2, column=2)
            Button(edit_usr_frame, text="Submit", bg="grey", command=amount).grid(row=2, column=3)

        def deleteUserUI():
            print("deleting users")
            clear_frame(edit_usr_frame)

            def removeUser():
                text = deleteUser(idVar.get())
                clear_frame(edit_usr_frame)
                accList()
                Label(edit_usr_frame, text=text).grid(row=2, column=1)

            idVar = StringVar()
            Label(edit_usr_frame, text="ID's for removal (separate with ,): ").grid(row=2, column=1)
            Entry(edit_usr_frame, textvariable=idVar).grid(row=2, column=2)
            Button(edit_usr_frame, text="Submit", bg="grey", command=removeUser).grid(row=2, column=3)

        def editUserName():
            print("editing user name")

        def change_dropdown(*args):
            if ddVar.get() == "Edit User Balance":
                editUserBalance()
            elif ddVar.get() == "Delete User":
                deleteUserUI()
            elif ddVar.get() == "Edit User Name":
                editUserName()

        ddVar.trace('w', change_dropdown)

    def toManager():
        clear_frame(first_frame)
        # exec(open("./managerUI.py").read())

    def backToCustLogin():
        clear_frame(first_frame)
        exec(open("./customerLoginUI.py").read())

    def firstFrame():
        Button(first_frame, text="Admin List", command=admList).grid(row=2, column=1)
        Button(first_frame, text="Accs List", command=accList).grid(row=2, column=2)
        Button(first_frame, text="Transaction Log", command=transLog).grid(row=2, column=3)
        Button(first_frame, text="Edit User", command=editUser).grid(row=3, column=1)
        Button(first_frame, text="Edit Admin/Manager", command=None).grid(row=3, column=2)  # THIS NEEDS DONE

        Button(first_frame, text="To Manager UI", command=toManager).grid(row=4, column=1)
        Button(first_frame, text="Back To Customer Login", bg="pink", command=backToCustLogin).grid(row=0, column=1)

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
