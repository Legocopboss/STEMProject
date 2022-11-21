from tkinter import *

from functionLibrary import *


def posUIDEF(idnum, root):
    root.title("Store UI")
    root.geometry("500x300")
    welcome_frame = Frame(root, bg="grey", width=400, height=75)
    welcome_frame.pack(side=TOP, expand=1, fill=BOTH)
    first_frame = Frame(root, bg="grey")
    first_frame.pack(side=RIGHT, expand=1, fill=BOTH)
    trans_frame = Frame(root, width=100, height=400, bg="grey")
    trans_frame.pack(side=LEFT, expand=1, fill=BOTH)

    def backToLogin():
        clear_frame(trans_frame, True)
        clear_frame(first_frame, True)
        clear_frame(welcome_frame, True)
        from customerLoginUI import customerLogin
        customerLogin(root)

    def removeFromTrans(item, price, invenID):
        for i in stockOfCurrentTrans:
            if i[0] == invenID:
                i[1] = i[1] + 1
        currentTrans.remove([item, price, invenID])
        posUIDEF.currtotal = posUIDEF.currtotal - price
        updateTransaction()

    def updateTransaction():
        clear_frame(trans_frame)
        print(currentTrans)
        t = 1
        Label(trans_frame, text="Current\nTransaction", font='Helvetica 10 bold').grid(row=0, column=1)
        for aI in currentTrans:
            tempI = Button(trans_frame, text=f"{aI[0]} {aI[1]}",
                           command=lambda it=aI[0], prc=aI[1], invenId=aI[2]: removeFromTrans(it, prc, invenId)).grid(
                row=t, column=1)
            t = t + 1
        Label(trans_frame, text=f"Total: {posUIDEF.currtotal}", font='Helvetica 10 bold').grid(row=t + 1, column=1)
        if posUIDEF.currtotal > 0:
            root.geometry(f"500x{str(300 + (26 * t))}")
            Button(trans_frame, text="Confirm Purchase", font="Helvetica 8 bold", bg="cyan",
                   command=confirmPurchase).grid(row=t + 2, column=1)
        Button(trans_frame, text="Back", bg="cyan", command=backToLogin).grid(row=t + 3, column=1)

    def addPurchase(item, price, invenID):
        stockInTrans = False
        for i in stockOfCurrentTrans:
            if i[0] == invenID:
                stockInTrans = True
                if i[1] - 1 <= 0:
                    messagebox.showerror("Oops!", f"Looks like we dont have enough of {item}.\nThe amount of this item "
                                                  f"in your current transaction is the most that can be added at this time. "
                                                  f"Sorry for the inconvenience!")
                    break
                else:
                    i[1] = i[1] - 1
                    currentTrans.append([item, price, invenID])
                    posUIDEF.currtotal = posUIDEF.currtotal + price
                    break
            else:
                stockInTrans = False

        if not stockInTrans:
            stockOfCurrentTrans.append([invenID, getStock(invenID) - 1])
            currentTrans.append([item, price, invenID])
            posUIDEF.currtotal = posUIDEF.currtotal + price

        print(posUIDEF.currtotal)
        updateTransaction()

    def confirmPurchase():
        purchasesT = sorted(currentTrans, key=lambda z: z[1], reverse=TRUE)
        purchases = purchasesT
        receipt = []
        print(purchases.count(purchases[0]))
        while len(purchases) != 0:
            receipt.append("" + str(purchases.count(purchases[0])) + "x " + str(purchases[0]))
            purchases = [i for i in purchases if i != purchases[0]]
        print(receipt)
        receipt = str(receipt).replace("\'", "")
        newTransaction(idnum, receipt, -posUIDEF.currtotal)
        for all in currentTrans:
            addInven(-1, all[2])
            InventoryCHECK(all[2])

        clear_frame(trans_frame, True)
        clear_frame(first_frame, True)
        clear_frame(welcome_frame)
        Label(welcome_frame, text="Purchase Successful").pack()
        Label(welcome_frame, text="Receipt: " + receipt).pack()
        Label(welcome_frame, text="Total: " + str(posUIDEF.currtotal)).pack()
        Button(welcome_frame, text="Back To Login", bg="cyan", command=backToLogin).pack()

    posUIDEF.currtotal = 0.0
    stockOfCurrentTrans = []
    currentTrans = []

    Label(welcome_frame,
          text=f"Welcome {printInfo(idnum, 2)}. You have a balance of {printInfo(idnum, 3)} Braden Bux ©").pack()

    def POSButtons():
        items = allItems_VersionInventory()
        x = 0
        y = 1
        lim = int(len(items) ** 0.5)
        for li in items:
            print(li)
            templ = Button(first_frame, text=f"{li[1]}\n{li[2]}",
                           command=lambda it=li[1], prc=li[2], invenID=li[3]: addPurchase(it, prc, invenID),
                           bg='pale turquoise').grid(row=y, column=x, sticky="NSEW")
            if x + 1 == lim:
                x = 0
                y = y + 1
            x = x + 1

    POSButtons()
    updateTransaction()


if __name__ == "__customerLoginUI__":
    posUIDEF()
