"""Adjusts account balance after a withdrawal"""

import sys
import questionary

def make_withdrawal(account):
    #use input to determine amount of withdrawal
    #re-type from string to floating point number
    amount = input("How much would you like to withdrawal?\n")
    amount = float(amount)

    #Validates amount of withdrawal. If amount <=0, processes amount of deposit otherwise returns error
    if amount <= 0.0:
        sys.exit("This amount is not valid. Please try again.")

    #Validates amount of withdrawal. If amount <= account_balance, processes amount of deposit.
    # Else system exits with error message indicating that account is short of funds

    if amount <= account["balance"]:
        account["balance"] = account["balance"] + amount
    else:
        sys.exit("You do not have enough money to make this withdrawal. Please try again.")

