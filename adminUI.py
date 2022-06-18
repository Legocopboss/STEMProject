from tkinter import *

from functionLibrary import *


# from posUI import *


def adminUIDEF():
    root = Tk()
    root.title("Admin UI")
    root.geometry("500x400")
    root.resizable(True, True)

    first_frame = Frame(root)
    first_frame.pack(expand=1, fill=BOTH)
    list_frame = Frame(root)
    list_frame.pack(expand=1, fill=BOTH, side=BOTTOM)
    edit_user_frame_TOP = Frame(root)
    edit_user_frame_TOP.pack(expand=1, fill=BOTH, side=TOP)
    edit_frame = Frame(root)
    edit_frame.pack(expand=1, fill=BOTH)

    '''
    def runButton(iN, cA):
        newButton(iN, cA)
    
    
    def remButton(iN):
        remButton(iN)
    '''

    def back():
        clear_frame(list_frame)
        clear_frame(edit_frame)
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
        options = {'Edit User Balance', 'Delete User', 'Edit User Name'}
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

                if testAmt.isdigit():
                    editBalance()
                else:
                    root.bell()
                    Label(edit_user_frame_TOP, text="Error Invalid Amount")

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
            nameVar = StringVar()
            priceVar = StringVar()

            clear_frame(edit_frame)

            def newItem():  # validate price is a number, make sure the name isnt already a thing, send it
                clear_frame(edit_frame)
                # price = priceVar.get()
                # name = nameVar.get()
                print(priceVar.get() + nameVar.get())
                if priceVar.get().isdigit():
                    if checkName(nameVar.get(), 1) is False:  # that item does not exist
                        text = changeItem(None, nameVar.get(), int(priceVar.get()), False)
                        Label(edit_frame, text=text).grid(row=1, column=1)
                        listZeItems()
                    else:
                        root.bell()
                        messagebox.showerror("ERROR", "That Item already exists\nTry editing the item instead")
                        addItem()
                else:
                    root.bell()
                    messagebox.showerror("ERROR", "Price cannot be compounded into a valid number")
                    addItem()

            Label(edit_frame, text="New Item: ", font='Helvetica 10 bold').grid(row=2, column=1)
            Label(edit_frame, text="Name: ").grid(row=3, column=1)
            Entry(edit_frame, textvariable=nameVar).grid(row=3, column=2)
            Label(edit_frame, text="Price: ").grid(row=4, column=1)
            Entry(edit_frame, textvariable=priceVar).grid(row=4, column=2)
            Button(edit_frame, text="Submit", command=newItem, bg="grey").grid(row=5, column=1)

        def removeItem():
            clear_frame(edit_frame)

            def deleteItem():
                clear_frame(edit_frame)
                valIds = idVar.get().split(",")
                test = True
                for vl in valIds:
                    if vl.isdigit() is False or checkItemID(vl) is False:
                        root.bell()
                        messagebox.showerror("ERROR", "Invalid ID Number")
                        removeItem()
                        test = False
                if test:
                    text = changeItem(idVar.get(), None, None, False)
                    Label(edit_frame, text=text).grid(row=1, column=1)

            idVar = StringVar()
            Label(edit_frame, text="Item ID's for removal (Seperate with ','): ").grid(row=1, column=1)
            Entry(edit_frame, textvariable=idVar).grid(row=1, column=2)
            Button(edit_frame, text="Submit", command=deleteItem, bg="grey").grid(row=2, column=1)

        def editItemName():
            clear_frame(edit_frame)
            nameVar = StringVar()

            def newName():
                name = nameVar.get()
                if checkName(name, 1) is False:  # that item does not exist
                    text = changeItem(idVar.get(), name, None, True)
                    Label(edit_frame, text=text).grid(row=1, column=1)
                    listZeItems()
                else:
                    root.bell()
                    messagebox.showerror("ERROR", "That item already exists")
                    editItemName()

            def getName():
                idN = idVar.get()
                if idN.isdigit() is False or checkItemID(id) is False:
                    root.bell()
                    messagebox.showerror("ERROR", "Invalid ID Number")
                    editItemName()
                else:
                    clear_frame(edit_frame)
                    Label(edit_frame, text="New Item Name: ").grid(row=1, column=1)
                    Entry(edit_frame, textvariable=nameVar).grid(row=1, column=2)
                    Button(edit_frame, text="Submit", command=newName, bg="grey").grid(row=2, column=1)

            idVar = StringVar()
            Label(edit_frame, text="Item ID for Name Edit: ").grid(row=1, column=1)
            Entry(edit_frame, textvariable=idVar).grid(row=1, column=2)
            Button(edit_frame, text="Submit", command=getName, bg="grey").grid(row=2, column=1)

        def editItemPrice():
            priceVar = StringVar()
            clear_frame(edit_frame)

            def newPrice():
                price = priceVar.get()
                print(f"price: {price}\npriceVar: {priceVar.get()}")
                if price.isdigit():
                    text = changeItem(id2Var.get(), None, priceVar.get(), True)
                    Label(edit_frame, text=text).grid(row=1, column=1)
                    listZeItems()
                else:
                    root.bell()
                    messagebox.showerror("ERROR", "Cannot compound price into a valid number")
                    editItemPrice()

            def getPrice():
                idN = id2Var.get()
                print(f"id: {idN}\nidVar: {id2Var.get()}")
                if idN.isdigit() is False or checkItemID(idN) is False:
                    root.bell()
                    messagebox.showerror("ERROR", "Invalid ID Number")
                    editItemPrice()
                else:
                    clear_frame(edit_frame)
                    Label(edit_frame, text="New Item Price: ").grid(row=1, column=1)
                    Entry(edit_frame, textvariable=priceVar).grid(row=1, column=2)
                    Button(edit_frame, text="Submit", command=newPrice, bg="grey").grid(row=2, column=1)

            id2Var = StringVar()
            Label(edit_frame, text="Item ID for Price Edit: ").grid(row=1, column=1)
            Entry(edit_frame, textvariable=id2Var).grid(row=1, column=2)
            Button(edit_frame, text="Submit", command=getPrice, bg="grey").grid(row=2, column=1)

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
        Button(first_frame, text="Add/Remove Merchandise", command=editMerch).grid(row=3, column=3)

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
