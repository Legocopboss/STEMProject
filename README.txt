POS System

over 1,539 lines of code (checked 11/20/2022 4:32 PM CST)



Little Details:
-LOTS of safety nets to catch bad information or inputs
-Auto Removes item from pos if the inventory stock is < 5
-When editing an admin/manager it will check if they are an illegal combination
(You can be manager without being admin but not vis versa) and will make an adjustment as needed
-In Admin/manager edit screen you cannot edit yourself (that would be stupid)
-When adding a purchase to the current transaction it will check the stock to make sure that the
item can actually be sold
