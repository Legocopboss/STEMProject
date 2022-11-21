from tkinter import *

from functionLibrary import *


def ManagerUIFrame(root, uname=None):
    clear_root(root)
    root.title("Manager UI")

    first_frame = Frame(root, bg="grey", height=0)
    first_frame.pack(expand=0, fill=BOTH)
    first_frame.grid_propagate(1)
    edit_user_frame_TOP = Frame(root, bg="grey", height=0)
    edit_user_frame_TOP.pack(expand=1, fill=BOTH, side=TOP)
    edit_frame = Frame(root, bg="grey", height=0)
    edit_frame.pack(expand=1, fill=BOTH)
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

    def back():
        clear_frame(list_frame, True)
        clear_frame(edit_frame, True)
        clear_frame(edit_user_frame_TOP, True)
        ManagerUIFrame(root, uname)

    def addI(amt, id):
        addInven(amt, id)
        listInventory()

    def addToPOS(invenID, name):
        if getStock(invenID) <= 5:
            root.bell()
            messagebox.showerror("Error",
                                 "This item has less than 5 in stock meaning it cannot be added to the POS system")
            return

        clear_frame(edit_frame)

        def checkPrice():
            if check_if_float(priceVar.get()):
                text = newItem_VersionInventory(name, priceVar.get(), invenID)
                clear_frame(edit_frame)
                listInventory()
                Label(edit_frame, text=text).grid(row=2, column=1, sticky="NSEW")
            else:
                root.bell()
                messagebox.showerror("Error", "Price not valid")
                addToPOS(invenID, name)

        priceVar = StringVar()
        Label(edit_frame, text=f"Price of {name}: ").grid(row=2, column=1, sticky="NSEW")
        Entry(edit_frame, textvariable=priceVar).grid(row=2, column=2, sticky="NSEW")
        Button(edit_frame, text="Submit", bg="grey", command=checkPrice).grid(row=2, column=3, sticky="NSEW")

    def removeFromPOS(invenID):
        clear_frame(edit_frame)
        itemID = getItemFromInvenID(invenID)
        print(itemID)
        removeItem_VersionInventory(itemID)
        listInventory()

    def listInventory():
        clear_frame(list_frame)
        clear_frame(first_frame)
        inven = viewInventory()

        Label(list_frame, text="ID", font='Helvetica 10 bold').grid(row=1, column=1, sticky='NSEW')
        Label(list_frame, text="Merchandise", font='Helvetica 10 bold').grid(row=1, column=2, sticky='NSEW')
        Label(list_frame, text="Stock", font='Helvetica 10 bold').grid(row=1, column=3, sticky='NSEW')
        x = 2
        for li in inven:
            Label(list_frame, text=li[0]).grid(row=x, column=1, sticky="NSEW")
            Label(list_frame, text=li[1]).grid(row=x, column=2, sticky="NSEW")
            Label(list_frame, text=li[2]).grid(row=x, column=3, sticky="NSEW")
            Button(list_frame, text="+1", command=lambda amt=1, id=li[0]: addI(amt, id), bg="green").grid(row=x,
                                                                                                          column=4,
                                                                                                          sticky="NSEW")
            Button(list_frame, text="+5", command=lambda amt=5, id=li[0]: addI(amt, id), bg="green").grid(row=x,
                                                                                                          column=5,
                                                                                                          sticky="NSEW")
            Button(list_frame, text="+10", command=lambda amt=10, id=li[0]: addI(amt, id), bg="green").grid(row=x,
                                                                                                            column=6,
                                                                                                            sticky="NSEW")
            Button(list_frame, text="-10", command=lambda amt=-10, id=li[0]: addI(amt, id), bg="red").grid(row=x,
                                                                                                           column=7,
                                                                                                           sticky="NSEW")
            Button(list_frame, text="-5", command=lambda amt=-5, id=li[0]: addI(amt, id), bg="red").grid(row=x,
                                                                                                         column=8,
                                                                                                         sticky="NSEW")
            Button(list_frame, text="-1", command=lambda amt=-1, id=li[0]: addI(amt, id), bg="red").grid(row=x,
                                                                                                         column=9,
                                                                                                         sticky="NSEW")
            if not checkIfInvenIsInPOS(li[0]):
                Button(list_frame, text="Add To POS", command=lambda invenID=li[0], name=li[1]: addToPOS(invenID, name),
                       bg="pale green").grid(row=x, column=10, sticky="NSEW")
            else:
                Button(list_frame, text="Remove From POS", command=lambda invenID=li[0]: removeFromPOS(invenID),
                       bg="indian red").grid(row=x, column=10, sticky="NSEW")
            x = x + 1
        Button(list_frame, text="Back", bg="cyan", command=back).grid(row=x + 1, column=1, sticky='NSEW')
        scrollbar.pack(side=RIGHT, fill=Y, expand=FALSE)
        list_frame_C.pack(expand=1, fill=BOTH, side=LEFT)

    def manageInven():
        listInventory()
        options = {'Add Item', 'Remove Item'}
        ddVar = StringVar(root)
        ddVar.set('Add Item')
        popupMenu = OptionMenu(edit_user_frame_TOP, ddVar, *options)
        Label(edit_user_frame_TOP, text="Options: ").grid(row=1, column=1, sticky='NSEW')
        popupMenu.grid(row=1, column=2, sticky='NSEW')

        def addItemInInven():
            amt = StringVar()
            clear_frame(edit_frame)

            def getName():
                clear_frame(edit_frame)
                if not checkInvenForName(nameVar.get(), 1):
                    Label(edit_frame, text="Starting amount of merchandise in inventory: ").grid(row=2, column=1,
                                                                                                 sticky="NSEW")
                    Entry(edit_frame, textvariable=amt).grid(row=2, column=2, sticky='NSEW')
                    Button(edit_frame, text="Submit", bg="grey", command=addItem).grid(row=2, column=3, sticky='NSEW')
                else:
                    root.bell()
                    messagebox.showerror("Error", f"Name {nameVar.get()} Invalid, might already exist in Database")
                    addItemInInven()

            def addItem():
                clear_frame(edit_frame)
                if check_if_int(amt.get()):
                    text = addNewToInventory(nameVar.get(), int(amt.get()))
                    clear_frame(edit_frame)
                    listInventory()
                    Label(edit_frame, text=text).grid(row=2, column=1, sticky="NSEW")
                else:
                    root.bell()
                    messagebox.showerror("Error", "Invalid amount")
                    addItemInInven()

            nameVar = StringVar()
            Label(edit_frame, text="Merchandise Name to be added to inventory: ").grid(row=2, column=1, sticky="NSEW")
            Entry(edit_frame, textvariable=nameVar).grid(row=2, column=2, sticky="NSEW")
            Button(edit_frame, text="Submit", bg="grey", command=getName).grid(row=2, column=3, sticky="NSEW")

        def removeItem():
            clear_frame(edit_frame)

            def checkID():
                clear_frame(edit_frame)
                if checkInvenForID(idVar.get()):
                    if checkIfInvenIsInPOS(idVar.get()):
                        removeFromPOS(idVar.get())
                    removeFromInventory(idVar.get())
                    listInventory()
                else:
                    root.bell()
                    messagebox.showerror("Error", f"ID number not found in database")
                    removeItem()

            idVar = StringVar()
            Label(edit_frame, text="Merchandise item ID to be removed from inventory: ").grid(row=2, column=1,
                                                                                              sticky="NSEW")
            Entry(edit_frame, textvariable=idVar).grid(row=2, column=2, sticky="NSEW")
            Button(edit_frame, text="Submit", bg="grey", command=checkID).grid(row=2, column=3, sticky="NSEW")

        def change_dropdown(*args):
            if ddVar.get() == "Add Item":
                addItemInInven()
            elif ddVar.get() == "Remove Item":
                removeItem()

        ddVar.trace('w', change_dropdown)

    def backToCustLogin():
        clear_frame(first_frame, True)
        from customerLoginUI import customerLogin
        customerLogin(root)

    def firstFrame():
        Button(first_frame, text='Manage Inventory', command=manageInven).grid(row=2, column=1, sticky='NSEW')

        Button(first_frame, text="Back To Customer Login", bg='cyan', command=backToCustLogin).grid(row=0, column=1,
                                                                                                    sticky="NSEW")

    firstFrame()

if __name__ == "__adminUI__":
    ManagerUIFrame()
