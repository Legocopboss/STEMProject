from tkinter import *

from functionLibrary import *


def posUIDEF(idnum, root):
    root.title("Store UI")
    root.geometry("400x200")
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

    def removeFromTrans(item, price):
        currentTrans.remove([item, price])
        posUIDEF.currtotal = posUIDEF.currtotal - price
        updateTransaction()

    def updateTransaction():
        clear_frame(trans_frame)
        print(currentTrans)
        t = 1
        Label(trans_frame, text="Current\nTransaction", font='Helvetica 10 bold').grid(row=0, column=1)
        for aI in currentTrans:
            tempI = Button(trans_frame, text=aI, command=lambda it=aI[0], prc=aI[1]: removeFromTrans(it, prc)).grid(
                row=t, column=1)
            t = t + 1
        Label(trans_frame, text=f"Total: {posUIDEF.currtotal}", font='Helvetica 10 bold').grid(row=t + 1, column=1)
        if posUIDEF.currtotal > 0:
            root.geometry(f"400x{str(200 + (26 * t))}")
            Button(trans_frame, text="Confirm Purchase", font="Helvetica 8 bold", bg="cyan",
                   command=confirmPurchase).grid(row=t + 2, column=1)
        Button(trans_frame, text="Back", bg="cyan", command=backToLogin).grid(row=t + 3, column=1)

    def addPurchase(item, price):
        currentTrans.append([item, price])
        posUIDEF.currtotal = posUIDEF.currtotal + price
        print(posUIDEF.currtotal)
        updateTransaction()

    def confirmPurchase():
        purchasesT = sorted(currentTrans, key=lambda z: z[1], reverse=TRUE)
        purchases = str(purchasesT).replace('\'', '')
        print(purchases)
        newTransaction(idnum, purchases, -posUIDEF.currtotal)
        clear_frame(trans_frame, True)
        clear_frame(first_frame, True)
        clear_frame(welcome_frame)
        Label(welcome_frame, text="Purchase Successful").pack()
        Label(welcome_frame, text="Receipt: " + purchases).pack()
        Label(welcome_frame, text="Total: " + str(posUIDEF.currtotal)).pack()
        Button(welcome_frame, text="Back To Login", bg="cyan", command=backToLogin).pack()

    posUIDEF.currtotal = 0.0
    currentTrans = []
    items = allItems()

    Label(welcome_frame,
          text=f"Welcome {printInfo(idnum, 2)}. You have a balance of {printInfo(idnum, 3)} Braden Bux ©").pack()

    x = 0
    for li in items:
        print(li)
        templ = Button(first_frame, text=f"{li[0]}\n{li[1]}",
                       command=lambda it=li[0], prc=li[1]: addPurchase(it, prc)).grid(row=x, column=1)
        x = x + 1

    updateTransaction()


if __name__ == "__customerLoginUI__":
    posUIDEF()
