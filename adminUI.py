from posUI import *

root = Tk()


def run():
    None


itemName = Tk.Entry(root, text="Item Name: ").grid(row=1, column=1)
itemCharge = Tk.Entry(root, text="Item price: ").grid(row=1, column=2)


def runButton(iN, cA):
    posUI.newButton(iN, cA)


def remButton(iN):
    posUI.remButton(iN)


addButton = Tk.Button(root, text="Add Button", command=runButton(itemName, itemCharge), state=DISABLED).grid(row=2,
                                                                                                             column=1)
removeButton = Tk.Button(root, text="Remove Button", command=remButton(itemName)).grid(row=2, column=2)

formLabel = Tk.Label(text="One of the fields above is not filled out.", state=DISABLED).pack()

if (itemName != "" and itemCharge != ""):
    addButton['state'] = Tk.NORMAL
elif (itemName == "" or itemCharge == ""):
    formLabel['state'] = Tk.NORMAL

root.mainloop()
