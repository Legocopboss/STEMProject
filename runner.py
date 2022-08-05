from tkinter import *

from customerLoginUI import customerLogin

exec(open("./database.py").read())

root = Tk()
root.geometry("400x400")
root.resizable(True, True)

customerLogin(root)

root.mainloop()

# exec(open("./customerLoginUI.py").read())
# from adminUI import adminUIDEF

# adminUIDEF()
