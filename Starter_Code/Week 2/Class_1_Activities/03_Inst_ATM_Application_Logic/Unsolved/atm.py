"""This is a basic ATM Application.

This is a command line application that mimics the actions of an ATM.

Example:
    $ python app.py
"""
import sys

from utils import (
    
)
accounts = [
    {
    "pin": 123456,
    "balance" : 1436.19},
    {
    "pin" : 246802,
    "balance": 3571.87},
    {
    "pin": 135791,
    "balance" : 543.79},
    {
    "pin" : 123987,
    "balance": 25.89},
    {
    "pin" : 269731,
    "balance": 3258.42}
]

#Enter pin and check account balance
def login():
    pin = input("Please input the pin: ")
    for account in accounts:
        if int(pin) == account["pin"]:
            print(f"The account balance for PIN {account['pin']} is {account['balance']}")
    else:
        return "Doesn't exist"
        
account_balance = login()
print(account_balance)






