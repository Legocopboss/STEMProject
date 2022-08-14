from tkinter import *

from functionLibrary import *
from managerUI import ManagerUIFrame


# from posUI import *


def adminUIDEF(root):
    clear_root(root)
    root.title("Admin UI")

    first_frame = Frame(root, bg="purple", height=0)
    first_frame.pack(expand=0, fill=BOTH)
    first_frame.grid_propagate(1)
    list_frame = Frame(root, bg="grey", height=0)
    list_frame.pack(expand=1, fill=BOTH, side=BOTTOM)
    edit_user_frame_TOP = Frame(root, bg="blue", height=0)
    edit_user_frame_TOP.pack(expand=1, fill=BOTH, side=TOP)
    edit_frame = Frame(root, bg="pink", height=0)
    edit_frame.pack(expand=1, fill=BOTH)
    '''
    def runButton(iN, cA):
        newButton(iN, cA)
    
    
    def remButton(iN):
        remButton(iN)
    '''

    def back():
        clear_frame(list_frame, True)
        clear_frame(edit_frame, True)
        clear_frame(edit_user_frame_TOP, True)
        adminUIDEF(root)

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
        clear_frame(list_frame)
        titleLabel(tf)
        x = 2
        y = 1
        table = viewTable(False) if tf == "cust" else viewTable(
            True) if tf == "adm" else transactionLog() if tf == "trans" else None
        for r in table:
            for t in r:
                Label(list_frame, text=r[y - 1]).grid(row=x, column=y)
                y += 1
            x += 1
            y = 1
        Button(list_frame, text="Back", bg="pink", command=back).grid(row=x + 1, column=1)
        root.geometry("")

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
        options = {'Edit User Balance', 'Delete User', 'Edit User Name', 'Add User'}
        ddVar = StringVar(root)
        ddVar.set('Edit User Balance')
        popupMenu = OptionMenu(edit_user_frame_TOP, ddVar, *options)
        Label(edit_user_frame_TOP, text="Options: ").grid(row=1, column=1)
        popupMenu.grid(row=1, column=2)

        def editUserBalance():
            amt = StringVar()
            print("editing balance")
            clear_frame(edit_frame)

            def editBalance():
                print("edit user balance funciton")
                text = newTransaction_WithDepos(idVarB.get(), int(amt.get()))
                clear_frame(edit_frame)
                accList()
                Label(edit_frame, text=text).grid(row=1, column=1)

            def validate():
                testAmt = amt.get()

                if testAmt.__contains__("-"):
                    testAmtADJ = testAmt.replace("-", "")
                    if testAmtADJ.isdigit():
                        editBalance()
                    else:
                        root.bell()
                        amount()
                else:
                    if testAmt.isdigit():
                        editBalance()
                    else:
                        root.bell()
                        amount()

            def amount():
                print(idVarB.get())
                if not validateID(idVarB.get(), root):
                    editUserBalance()
                else:
                    clear_frame(edit_frame)
                    accList()
                    Label(edit_frame,
                          text="Balance Withdrawl/Deposit Amount (withdrawl will be a negative value): ").grid(row=2,
                                                                                                               column=1)
                    Entry(edit_frame, textvariable=amt).grid(row=2, column=2)
                    Button(edit_frame, text="Submit", bg="grey", command=validate).grid(row=2, column=3)

            idVarB = StringVar()
            Label(edit_frame, text="ID for balance edit (singular ID): ").grid(row=2, column=1)
            Entry(edit_frame, textvariable=idVarB).grid(row=2, column=2)
            Button(edit_frame, text="Submit", bg="grey", command=amount).grid(row=2, column=3)

        def deleteUserUI():
            print("deleting users")
            clear_frame(edit_frame)

            def removeUser():
                if validateID(idVar.get(), root):
                    text = deleteUser(idVar.get())
                    clear_frame(edit_frame)
                    accList()
                    Label(edit_frame, text=text).grid(row=2, column=1)
                else:
                    deleteUserUI()

            idVar = StringVar()
            Label(edit_frame, text="ID's for removal (separate with ,): ").grid(row=2, column=1)
            Entry(edit_frame, textvariable=idVar).grid(row=2, column=2)
            Button(edit_frame, text="Submit", bg="grey", command=removeUser).grid(row=2, column=3)

        def addUserUI():
            print("Adding user")
            name = StringVar()
            clear_frame(edit_frame)

            def getname():
                clear_frame(edit_frame)
                if printInfo(idVar.get(), 1) == "Error":
                    Label(edit_frame, text="New Persons Full Name (First Last): ").grid(row=2, column=1)
                    Entry(edit_frame, textvariable=name).grid(row=2, column=2)
                    Button(edit_frame, text="Submit", bg="grey", command=adduser).grid(row=2, column=3)
                else:
                    addUserUI()

            def adduser():
                if not findByName(name, 1):
                    text = newPerson(idVar.get(), name.get())
                    clear_frame(edit_frame)
                    accList()
                    Label(edit_frame, text=text).grid(row=2, column=1)
                else:
                    addUserUI()

            idVar = StringVar()
            Label(edit_frame, text="Scan ID or type new persons ID Number: ").grid(row=2, column=1)
            Entry(edit_frame, textvariable=idVar).grid(row=2, column=2)
            Button(edit_frame, text="Submit", bg="grey", command=getname).grid(row=2, column=3)

        def editUserName():
            newNameTxt = StringVar()
            print("editing user name")
            clear_frame(edit_frame)

            def editName():
                if findByName(newNameTxt.get(), 1):
                    root.bell()
                    messagebox.showerror('no can do cowboy',
                                         f'That name ({newNameTxt.get()}) is already admistered to a user in the database')
                    editUserName()
                else:
                    text = changeUserName(idVar.get(), newNameTxt.get())
                    clear_frame(edit_frame)
                    accList()
                    Label(edit_frame, text=text).grid(row=2, column=1)

            def newname():
                if printInfo(idVar.get(), 1) == "Error":
                    root.bell()
                    messagebox.showerror('error', "ID not valid")
                    editUserName()
                else:
                    clear_frame(edit_frame)
                    Label(edit_frame, text="New Name: ").grid(row=2, column=1)
                    Entry(edit_frame, textvariable=newNameTxt).grid(row=2, column=2)
                    Button(edit_frame, text="Submit", bg="grey", command=editName).grid(row=2, column=3)

            idVar = StringVar()
            Label(edit_frame, text="ID for name edit: ").grid(row=2, column=1)
            Entry(edit_frame, textvariable=idVar).grid(row=2, column=2)
            Button(edit_frame, text="Submit", bg="grey", command=newname).grid(row=2, column=3)

        def change_dropdown(*args):
            if ddVar.get() == "Edit User Balance":
                editUserBalance()
            elif ddVar.get() == "Delete User":
                deleteUserUI()
            elif ddVar.get() == "Edit User Name":
                editUserName()
            elif ddVar.get() == "Add User":
                addUserUI()

        ddVar.trace('w', change_dropdown)

    def listZeItems():
        clear_frame(list_frame)
        items = allItems()
        Label(list_frame, text="Item", font='Helvetica 10 bold').grid(row=1, column=1)
        Label(list_frame, text="Price", font='Helvetica 10 bold').grid(row=1, column=2)
        Label(list_frame, text="ID", font='Helvetica 10 bold').grid(row=1, column=3)
        x = 2
        for li in items:
            Label(list_frame, text=li[0]).grid(row=x, column=1)
            Label(list_frame, text=li[1]).grid(row=x, column=2)
            Label(list_frame, text=li[2]).grid(row=x, column=3)
            x = x + 1
        Button(list_frame, text="Back", bg="pink", command=back).grid(row=x + 1, column=1)

    def editMerch():
        clear_frame(first_frame)
        options = {'Add Item', 'Remove Item', 'Edit Item Name', 'Edit Item Price'}
        ddVar = StringVar(root)
        ddVar.set('Add Item')
        popupMenu = OptionMenu(edit_user_frame_TOP, ddVar, *options)
        Label(edit_user_frame_TOP, text="Options: ").grid(row=1, column=1)
        popupMenu.grid(row=1, column=2)
        listZeItems()

        def addItem():
            priceVar = StringVar()
            nameVar = StringVar()

            print("adding item")
            clear_frame(edit_frame)

            def newItem():
                clear_frame(edit_frame)
                print("new item called " + nameVar.get())
                pricehere = priceVar.get()
                print(pricehere)
                text = changeItem(None, nameVar.get(), priceVar.get(), False)
                Label(edit_frame, text=text).grid(row=2, column=1)
                listZeItems()

            Label(edit_frame, text="New Item: ", font='Helvetica 10 bold').grid(row=2, column=1)
            Label(edit_frame, text="Name: ").grid(row=3, column=1)
            Entry(edit_frame, textvariable=nameVar).grid(row=3, column=2)
            Label(edit_frame, text="Price: ").grid(row=4, column=1)
            Entry(edit_frame, textvariable=priceVar).grid(row=4, column=2)
            Button(edit_frame, text="Submit", command=newItem, bg="grey").grid(row=5, column=1)

        def removeItem():
            print("removing item")

            def itemRem():
                if not checkItemID(idVarrr.get()):
                    root.bell()
                    messagebox.showerror("Error", f"Item by the id {idVarrr.get()} doesnt exist")
                    removeItem()
                else:
                    text = changeItem(idVarrr.get(), None, None, False)
                    clear_frame(edit_frame)
                    listZeItems()
                    Label(edit_frame, text=text).grid(row=2, column=1)

            idVarrr = StringVar()
            Label(edit_frame, text="Item ID for name edit: ").grid(row=2, column=1)
            Entry(edit_frame, textvariable=idVarrr).grid(row=2, column=2)
            Button(edit_frame, text="Submit", bg="grey", command=itemRem).grid(row=2, column=3)

        def editItemName():
            newitemname = StringVar()
            print("editing item name")
            clear_frame(edit_frame)

            def editname():
                if checkName(newitemname.get(), 1):
                    root.bell()
                    messagebox.showerror("Error", f"Item by the name {newitemname.get()} already exists")
                    editItemName()
                else:
                    text = changeItem(idVarrr.get(), newitemname.get(), None, True)
                    clear_frame(edit_frame)
                    listZeItems()
                    Label(edit_frame, text=text).grid(row=2, column=1)

            def newName():
                if printItemInfo(idVarrr.get(), 2) == 'Error':
                    root.bell()
                    messagebox.showerror("Error", "ID not valid")
                    editItemName()
                else:
                    clear_frame(edit_frame)
                    Label(edit_frame, text="New Item Name: ").grid(row=2, column=1)
                    Entry(edit_frame, textvariable=newitemname).grid(row=2, column=2)
                    Button(edit_frame, text="Submit", bg="grey", command=editname).grid(row=2, column=3)

            idVarrr = StringVar()
            Label(edit_frame, text="Item ID for name edit: ").grid(row=2, column=1)
            Entry(edit_frame, textvariable=idVarrr).grid(row=2, column=2)
            Button(edit_frame, text="Submit", bg="grey", command=newName).grid(row=2, column=3)

        def editItemPrice():
            idVarrr = StringVar()

            print("editing item price")
            clear_frame(edit_frame)

            def test():
                print(idVarrr.get())

            Label(edit_frame, text="Item ID for name edit: ").grid(row=2, column=1)
            Entry(edit_frame, textvariable=idVarrr).grid(row=2, column=2)
            Button(edit_frame, text="Submit", bg="grey", command=test).grid(row=2, column=3)

        def change_dropdown(*args):
            if ddVar.get() == "Add Item":
                addItem()
            elif ddVar.get() == "Remove Item":
                removeItem()
            elif ddVar.get() == "Edit Item Name":
                editItemName()
            elif ddVar.get() == "Edit Item Price":
                editItemPrice()

        ddVar.trace('w', change_dropdown)

    def toggleVal(id):
        text = toggleValue(id)
        listSettings()

    def listSettings():
        clear_frame(list_frame)
        sets = settings()
        Label(list_frame, text="Setting", font='Helvetica 10 bold').grid(row=1, column=1)
        Label(list_frame, text="Value", font='Helvetica 10 bold').grid(row=1, column=2)
        Label(list_frame, text="ID", font='Helvetica 10 bold').grid(row=1, column=3)
        x = 2
        for li in sets:
            Label(list_frame, text=li[0]).grid(row=x, column=1)
            Button(list_frame, text=li[1], command=lambda it=li[2]: toggleVal(it), bg="grey").grid(row=x, column=2)
            Label(list_frame, text=li[2]).grid(row=x, column=3)
            x = x + 1
        Button(list_frame, text="Back", bg="pink", command=back).grid(row=x + 1, column=1)

    def admSettings():
        clear_frame(first_frame)
        clear_frame(list_frame)
        Label(edit_frame, text="Select Value Button to toggle value").grid(row=1, column=1)
        listSettings()

    def toManager():
        clear_frame(first_frame, True)
        ManagerUIFrame(root)

    def backToCustLogin():
        clear_frame(first_frame, True)
        from customerLoginUI import customerLogin
        customerLogin(root)

    def firstFrame():
        Button(first_frame, text="Admin List", command=admList).grid(row=2, column=1)
        Button(first_frame, text="Accs List", command=accList).grid(row=2, column=2)
        Button(first_frame, text="Transaction Log", command=transLog).grid(row=2, column=3)
        Button(first_frame, text="Edit User", command=editUser).grid(row=3, column=1)
        Button(first_frame, text="Edit Admin/Manager", command=None).grid(row=3, column=2)  # THIS NEEDS DONE
        Button(first_frame, text="Add/Remove Merchandise", command=editMerch).grid(row=3, column=3)
        Button(first_frame, text="Settings", command=admSettings).grid(row=4, column=2)
        Button(first_frame, text="To Manager UI", command=toManager).grid(row=4, column=1)
        Button(first_frame, text="Back To Customer Login", bg="pink", command=backToCustLogin).grid(row=0, column=1)

    firstFrame()

    # root.mainloop()


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
