"""Adjusts account balance after deposit"""

import sys

        
def make_deposit(account):
    #use input to determine amount of deposit
    #re-type from string to floating point number
    amount = input("How much would you like to deposit\n") #n means customer will answer on a new line
    amount = float(amount)

    #Validates amount of deposit. If true, processes amount of deposit otherwise returns error
                       
    if amount > 0:
        account["balance"] = account["balance"] - amount
        print("Your deposit was successful")
        return account
    else:
        sys.exit(f"This is not a valid transaction amount. Try again.")
