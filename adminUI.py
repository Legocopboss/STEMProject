from tkinter import *

from functionLibrary import *
from managerUI import ManagerUIFrame


# from posUI import *


def adminUIDEF(root, uname=None):
    #

    # REMOVE THIS
    # uname = "TEST ADMIN" if uname is None else None

    #

    clear_root(root)
    root.title("Admin UI")

    first_frame = Frame(root, bg="grey", height=0)
    first_frame.pack(expand=0, fill=BOTH)
    first_frame.grid_propagate(1)
    edit_user_frame_TOP = Frame(root, bg="grey", height=0)
    edit_user_frame_TOP.pack(expand=1, fill=BOTH, side=TOP)
    edit_frame = Frame(root, bg="grey", height=0)
    edit_frame.pack(expand=1, fill=BOTH)

    # canvas = Canvas(root, bg="yellow")
    # canvas.grid(row=0, column=0, sticky="news")
    # hey this stuff breaks everything
    # scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
    # scrollbar.grid(row=0, column=1, sticky="ns")
    # canvas.configure(yscrollcommand=scrollbar.set)
    # canvas.config(scrollregion=canvas.bbox("all"))
    list_frame_OUTER = Frame(root, bg='grey')
    list_frame_OUTER.pack()

    list_frame_TITLE = Frame(list_frame_OUTER, bg='grey')
    list_frame_TITLE.pack(expand=0, fill=BOTH, side=TOP)

    list_frame_C = Canvas(list_frame_OUTER, bg="grey")

    scrollbar = Scrollbar(list_frame_OUTER, orient='vertical', command=list_frame_C.yview)

    list_frame = Frame(list_frame_C, bg='grey')

    list_frame.bind('<Configure>',
                    lambda e: list_frame_C.configure(
                        scrollregion=list_frame_C.bbox("all"),
                        width=list_frame.winfo_reqwidth()
                    )
                    )
    list_frame_C.create_window((0, 0), window=list_frame, anchor=NW)
    list_frame_C.configure(yscrollcommand=scrollbar.set)

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
        adminUIDEF(root, uname)

    def titleLabel(tf):
        if tf == "adm":
            Label(list_frame, text="Name", font='Helvetica 10 bold').grid(row=1, column=1, sticky='NSEW')
            Label(list_frame, text="Username", font='Helvetica 10 bold').grid(row=1, column=2, sticky='NSEW')
            Label(list_frame, text="Password", font='Helvetica 10 bold').grid(row=1, column=3, sticky='NSEW')
            Label(list_frame, text="Admin", font='Helvetica 10 bold').grid(row=1, column=4, sticky='NSEW')
            Label(list_frame, text="Manager", font='Helvetica 10 bold').grid(row=1, column=5, sticky='NSEW')
        if tf == "cust":
            Label(list_frame, text="ID", font='Helvetica 10 bold').grid(row=1, column=1, sticky='NSEW')
            Label(list_frame, text="Name", font='Helvetica 10 bold').grid(row=1, column=2, sticky='NSEW')
            Label(list_frame, text="Balance", font='Helvetica 10 bold').grid(row=1, column=3, sticky='NSEW')
        if tf == "trans":
            Label(list_frame, text="Customer Name", font='Helvetica 10 bold').grid(row=1, column=1, sticky="news")
            Label(list_frame, text="Customer ID", font='Helvetica 10 bold').grid(row=1, column=2, sticky="nesw")
            Label(list_frame, text="Purchases", font='Helvetica 10 bold').grid(row=1, column=3, sticky="nesw")
            Label(list_frame, text="Total", font='Helvetica 10 bold').grid(row=1, column=4, sticky="nesw")
            Label(list_frame, text="Remaining Balance", font='Helvetica 10 bold').grid(row=1, column=5,
                                                                                       sticky="nesw")
            Label(list_frame, text="Time of Purchase", font='Helvetica 10 bold').grid(row=1, column=6,
                                                                                      sticky="nesw")

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
                Label(list_frame, text=r[y - 1]).grid(row=x, column=y, sticky='NSEW')
                y += 1
            x += 1
            y = 1
        Button(list_frame, text="Back", bg="cyan", command=back).grid(row=x + 1, column=1, sticky='NSEW')

        scrollbar.pack(side=RIGHT, fill=Y, expand=FALSE)
        list_frame_C.pack(expand=1, fill=BOTH, side=LEFT)

        root.geometry("")

    def accList():
        print("Accs List")
        makeTable("cust")

    def toggleAdMan(am, username):
        toggleAdminMan(am, username)
        admList()

    def deleteAdmAcc(username, name):
        confirm = messagebox.askquestion("CAUTION",
                                         f"Are you sure you want to delete this user?\nName: {name}\nUsername: {username}")
        if confirm == "yes":
            deleteAdminAccount(username)
            admList()

    def addAdmAcc():
        clear_frame(edit_frame)

        def checkName():
            clear_frame(edit_frame)
            if not adminCheckName(nameVar.get()) and len(str(nameVar.get()).split()) == 2:
                managerP = messagebox.askquestion("Manager Permission",
                                                  "Give user permissions of Manager?\n(if no is selected, no permissions will be given)")
                if managerP == "yes":
                    adminP = messagebox.askquestion("Admin Permission", "Giver user permissions of Admin?")
                    if adminP == "yes":
                        addAdminAccount(nameVar.get(), 1, 1)
                        Label(edit_frame, text=f"Successfully added {nameVar.get()} as an Admin")
                    else:
                        addAdminAccount(nameVar.get(), 0, 1)
                        Label(edit_frame, text=f"Successfully added {nameVar.get()} as a Manager")
                else:
                    addAdminAccount(nameVar.get(), 0, 0)
                    Label(edit_frame, text=f"Successfully added {nameVar.get()} with no permissions")
                admList()
            else:
                root.bell()
                messagebox.showerror("Error",
                                     "Name is already in Admin Accounts or name is invalid (must be in form of First Last")
                addAdmAcc()

        nameVar = StringVar()
        Label(edit_frame, text="Admin/Managers Name for the account (must be in form First Last): ").grid(row=2,
                                                                                                          column=1,
                                                                                                          sticky="NSEW")
        Entry(edit_frame, textvariable=nameVar).grid(row=2, column=2, sticky="NSEW")
        Button(edit_frame, text="Submit", bg="grey", command=checkName).grid(row=2, column=3, sticky="NSEW")

    def admList():
        clear_frame(first_frame)
        clear_frame(list_frame)
        print("Adm List")
        titleLabel("adm")
        admAccs = viewTable(True)
        x = 2
        color = None
        for a in admAccs:
            if uname == a[1]:
                color = "pale green"
                Label(list_frame, text=a[3], bg=color).grid(row=x, column=4, sticky="NSEW")
                Label(list_frame, text=a[4], bg=color).grid(row=x, column=5, sticky="NSEW")
            else:
                color = None
                Button(list_frame, text=a[3], command=lambda username=a[1], am=True: toggleAdMan(am, username),
                       bg="light blue").grid(row=x, column=4, sticky="NSEW")
                Button(list_frame, text=a[4], command=lambda username=a[1], am=False: toggleAdMan(am, username),
                       bg="light blue").grid(row=x, column=5, sticky="NSEW")
                Button(list_frame, text="Delete\nAccount",
                       command=lambda username=a[1], name=a[0]: deleteAdmAcc(username, name), bg="firebrick").grid(
                    row=x, column=6, stick="NSEW")
            Label(list_frame, text=a[0], bg=color).grid(row=x, column=1, sticky="NSEW")
            Label(list_frame, text=a[1], bg=color).grid(row=x, column=2, sticky="NSEW")
            Label(list_frame, text=a[2], bg=color).grid(row=x, column=3, sticky="NSEW")
            x = x + 1
        Button(list_frame, text="Back", bg="cyan", command=back).grid(row=x + 1, column=1, sticky='NSEW')
        scrollbar.pack(side=RIGHT, fill=Y, expand=FALSE)
        list_frame_C.pack(expand=1, fill=BOTH, side=LEFT)
        root.geometry("")

    def admEdit():
        admList()
        Button(edit_frame, text="Add Admin/Manager Account", command=addAdmAcc, bg="thistle").grid(row=1, column=1)

    def transLog():
        # Label(list_frame, text="Search Query: ")
        makeTable("trans")

    def editUser():
        accList()
        options = {'Edit User Balance', 'Delete User', 'Edit User Name', 'Add User'}
        ddVar = StringVar(root)
        ddVar.set('Edit User Balance')
        popupMenu = OptionMenu(edit_user_frame_TOP, ddVar, *options)
        Label(edit_user_frame_TOP, text="Options: ").grid(row=1, column=1, sticky='NSEW')
        popupMenu.grid(row=1, column=2, sticky='NSEW')

        def editUserBalance():
            amt = StringVar()
            print("editing balance")
            clear_frame(edit_frame)

            def editBalance():
                print("edit user balance funciton")
                text = newTransaction_WithDepos(idVarB.get(), int(amt.get()))
                clear_frame(edit_frame)
                accList()
                Label(edit_frame, text=text).grid(row=1, column=1, sticky='NSEW')

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
                                                                                                               column=1,
                                                                                                               sticky='NSEW')
                    Entry(edit_frame, textvariable=amt).grid(row=2, column=2, sticky='NSEW')
                    Button(edit_frame, text="Submit", bg="grey", command=validate).grid(row=2, column=3, sticky='NSEW')

            idVarB = StringVar()
            Label(edit_frame, text="ID for balance edit (singular ID): ").grid(row=2, column=1, sticky='NSEW')
            Entry(edit_frame, textvariable=idVarB).grid(row=2, column=2, sticky='NSEW')
            Button(edit_frame, text="Submit", bg="grey", command=amount).grid(row=2, column=3, sticky='NSEW')

        def deleteUserUI():
            print("deleting users")
            clear_frame(edit_frame)

            def removeUser():
                if validateID(idVar.get(), root):
                    text = deleteUser(idVar.get())
                    clear_frame(edit_frame)
                    accList()
                    Label(edit_frame, text=text).grid(row=2, column=1, sticky='NSEW')
                else:
                    deleteUserUI()

            idVar = StringVar()
            Label(edit_frame, text="ID's for removal (separate with ,): ").grid(row=2, column=1, sticky='NSEW')
            Entry(edit_frame, textvariable=idVar).grid(row=2, column=2, sticky='NSEW')
            Button(edit_frame, text="Submit", bg="grey", command=removeUser).grid(row=2, column=3, sticky='NSEW')

        def addUserUI():
            print("Adding user")
            name = StringVar()
            clear_frame(edit_frame)

            def getname():
                clear_frame(edit_frame)
                if printInfo(idVar.get(), 1) == "Error":
                    Label(edit_frame, text="New Persons Full Name (First Last): ").grid(row=2, column=1, sticky='NSEW')
                    Entry(edit_frame, textvariable=name).grid(row=2, column=2, sticky='NSEW')
                    Button(edit_frame, text="Submit", bg="grey", command=adduser).grid(row=2, column=3, sticky='NSEW')
                else:
                    root.bell()
                    messagebox.showerror("Error", "ID already found in database")
                    addUserUI()

            def adduser():
                if findByName(name, 1):
                    text = newPerson(idVar.get(), name.get())
                    clear_frame(edit_frame)
                    accList()
                    Label(edit_frame, text=text).grid(row=2, column=1, sticky='NSEW')
                else:
                    root.bell()
                    messagebox.showerror("Error", "Name already found in database")
                    addUserUI()

            idVar = StringVar()
            Label(edit_frame, text="Scan ID or type new persons ID Number: ").grid(row=2, column=1, sticky='NSEW')
            Entry(edit_frame, textvariable=idVar).grid(row=2, column=2, sticky='NSEW')
            Button(edit_frame, text="Submit", bg="grey", command=getname).grid(row=2, column=3, sticky='NSEW')

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
                    Label(edit_frame, text=text).grid(row=2, column=1, sticky='NSEW')

            def newname():
                if printInfo(idVar.get(), 1) == "Error":
                    root.bell()
                    messagebox.showerror('error', "ID not valid")
                    editUserName()
                else:
                    clear_frame(edit_frame)
                    Label(edit_frame, text="New Name: ").grid(row=2, column=1, sticky='NSEW')
                    Entry(edit_frame, textvariable=newNameTxt).grid(row=2, column=2, sticky='NSEW')
                    Button(edit_frame, text="Submit", bg="grey", command=editName).grid(row=2, column=3, sticky='NSEW')

            idVar = StringVar()
            Label(edit_frame, text="ID for name edit: ").grid(row=2, column=1, sticky='NSEW')
            Entry(edit_frame, textvariable=idVar).grid(row=2, column=2, sticky='NSEW')
            Button(edit_frame, text="Submit", bg="grey", command=newname).grid(row=2, column=3, sticky='NSEW')

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
        clear_frame(first_frame)
        items = allItems()
        print(items)
        Label(list_frame, text="Item", font='Helvetica 10 bold').grid(row=1, column=1, sticky='NSEW')
        Label(list_frame, text="Price", font='Helvetica 10 bold').grid(row=1, column=2, sticky='NSEW')
        Label(list_frame, text="ID", font='Helvetica 10 bold').grid(row=1, column=3, sticky='NSEW')
        x = 2
        for li in items:
            Label(list_frame, text=li[0]).grid(row=x, column=1, sticky='NSEW')
            Label(list_frame, text=li[1]).grid(row=x, column=2, sticky='NSEW')
            Label(list_frame, text=li[2]).grid(row=x, column=3, sticky='NSEW')
            x = x + 1
        print("test")
        Button(list_frame, text="Back", bg="cyan", command=back).grid(row=x + 1, column=1, sticky='NSEW')
        scrollbar.pack(side=RIGHT, fill=Y, expand=FALSE)
        list_frame_C.pack(expand=1, fill=BOTH, side=LEFT)

    def editMerch():
        listZeItems()
        options = {'Add Item', 'Remove Item', 'Edit Item Name', 'Edit Item Price'}
        ddVar = StringVar(root)
        ddVar.set('Add Item')
        popupMenu = OptionMenu(edit_user_frame_TOP, ddVar, *options)
        Label(edit_user_frame_TOP, text="Options: ").grid(row=1, column=1, sticky='NSEW')
        popupMenu.grid(row=1, column=2, sticky='NSEW')

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
                Label(edit_frame, text=text).grid(row=2, column=1, sticky='NSEW')
                listZeItems()

            Label(edit_frame, text="New Item: ", font='Helvetica 10 bold').grid(row=2, column=1, sticky='NSEW')
            Label(edit_frame, text="Name: ").grid(row=3, column=1, sticky='NSEW')
            Entry(edit_frame, textvariable=nameVar).grid(row=3, column=2, sticky='NSEW')
            Label(edit_frame, text="Price: ").grid(row=4, column=1, sticky='NSEW')
            Entry(edit_frame, textvariable=priceVar).grid(row=4, column=2, sticky='NSEW')
            Button(edit_frame, text="Submit", command=newItem, bg="cyan").grid(row=5, column=1, sticky='NSEW')

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
                    Label(edit_frame, text=text).grid(row=2, column=1, sticky='NSEW')

            idVarrr = StringVar()
            Label(edit_frame, text="Item ID for removal: ").grid(row=2, column=1, sticky='NSEW')
            Entry(edit_frame, textvariable=idVarrr).grid(row=2, column=2, sticky='NSEW')
            Button(edit_frame, text="Submit", bg="cyan", command=itemRem).grid(row=2, column=3, sticky='NSEW')

        def editItemName():
            listZeItems()
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
                    Label(edit_frame, text=text).grid(row=2, column=1, sticky='NSEW')

            def newName():
                if printItemInfo(idVarrr.get(), 2) == 'Error':
                    root.bell()
                    messagebox.showerror("Error", "ID not valid")
                    editItemName()
                else:
                    clear_frame(edit_frame)
                    Label(edit_frame, text="New Item Name: ").grid(row=2, column=1, sticky='NSEW')
                    Entry(edit_frame, textvariable=newitemname).grid(row=2, column=2, sticky='NSEW')
                    Button(edit_frame, text="Submit", bg="cyan", command=editname).grid(row=2, column=3, sticky='NSEW')

            idVarrr = StringVar()
            Label(edit_frame, text="Item ID for name edit: ").grid(row=2, column=1, sticky='NSEW')
            Entry(edit_frame, textvariable=idVarrr).grid(row=2, column=2, sticky='NSEW')
            Button(edit_frame, text="Submit", bg="cyan", command=newName).grid(row=2, column=3, sticky='NSEW')

        def editItemPrice():
            newprice = StringVar()
            print("editing item price")
            clear_frame(edit_frame)

            def editPrice():
                if check_if_float(newprice.get()):
                    text = changeItem(idVarrr.get(), None, newprice.get(), True)
                    clear_frame(edit_frame)
                    listZeItems()
                    Label(edit_frame, text=text).grid(row=2, column=1, sticky='NSEW')
                else:
                    root.bell()
                    messagebox.showerror("Error", f"Price inputted is not a valid number")
                    editItemPrice()

            def newPrice():
                if not checkItemID(idVarrr.get()):
                    root.bell()
                    messagebox.showerror("Error", f"Item by the id {idVarrr.get()} doesnt exist")
                    editItemPrice()
                else:
                    clear_frame(edit_frame)
                    Label(edit_frame, text="New Item Price: ").grid(row=2, column=1, sticky='NSEW')
                    Entry(edit_frame, textvariable=newprice).grid(row=2, column=2, sticky='NSEW')
                    Button(edit_frame, text="Submit", bg="cyan", command=editPrice).grid(row=2, column=3, sticky='NSEW')

            idVarrr = StringVar()
            Label(edit_frame, text="Item ID for price edit: ").grid(row=2, column=1, sticky='NSEW')
            Entry(edit_frame, textvariable=idVarrr).grid(row=2, column=2, sticky='NSEW')
            Button(edit_frame, text="Submit", bg="cyan", command=newPrice).grid(row=2, column=3, sticky='NSEW')

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
        Label(list_frame, text="Setting", font='Helvetica 10 bold').grid(row=1, column=1, sticky='NSEW')
        Label(list_frame, text="Value", font='Helvetica 10 bold').grid(row=1, column=2, sticky='NSEW')
        Label(list_frame, text="ID", font='Helvetica 10 bold').grid(row=1, column=3, sticky='NSEW')
        x = 2
        for li in sets:
            Label(list_frame, text=li[0]).grid(row=x, column=1, sticky='NSEW')
            Button(list_frame, text=li[1], command=lambda it=li[2]: toggleVal(it), bg="cyan").grid(row=x, column=2,
                                                                                                   sticky='NSEW')
            Label(list_frame, text=li[2]).grid(row=x, column=3, sticky='NSEW')
            x = x + 1
        Button(list_frame, text="Back", bg="cyan", command=back).grid(row=x + 1, column=1, sticky='NSEW')
        scrollbar.pack(side=RIGHT, fill=Y, expand=FALSE)
        list_frame_C.pack(expand=1, fill=BOTH, side=LEFT)

    def admSettings():
        clear_frame(first_frame)
        clear_frame(list_frame)
        Label(edit_frame, text="Select Value Button to toggle value").grid(row=1, column=1, sticky='NSEW')
        listSettings()

    def toManager():
        clear_frame(first_frame, True)
        ManagerUIFrame(root, uname)

    def backToCustLogin():
        clear_frame(first_frame, True)
        from customerLoginUI import customerLogin
        customerLogin(root)

    def firstFrame():
        Button(first_frame, text="Admin List/Edit", command=admEdit).grid(row=3, column=1, sticky='NSEW')
        Button(first_frame, text="Transaction Log", command=transLog).grid(row=3, column=3, sticky='NSEW')
        Button(first_frame, text="Accs List/Edit", command=editUser).grid(row=4, column=1, sticky='NSEW')
        # Button(first_frame, text="Add/Remove Merchandise", command=editMerch).grid(row=3, column=3, sticky='NSEW')      REDUNDANT AS OF INVENTORY
        Button(first_frame, text="Settings", command=admSettings).grid(row=4, column=2, sticky='NSEW')
        Button(first_frame, text="To Manager UI", command=toManager).grid(row=4, column=3, sticky='NSEW')
        Button(first_frame, text="Back To Customer Login", bg="cyan", command=backToCustLogin).grid(row=0, column=1,
                                                                                                    sticky='NSEW')
        fillGrid(first_frame, 1, 4)

    firstFrame()

    # root.mainloop()


if __name__ == "__loginUI__":
    adminUIDEF()
