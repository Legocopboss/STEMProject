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



