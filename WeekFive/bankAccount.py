'''
Problem:
Create a BankAccount class that simulates a simple bank account.

Attritbutes:
    account_holder:
    balance:
    
 Methods:
    deposit(Amount):
    withdraw(amount):
    sufficient funds,otherwise print error.
    display_balance():   

Author:Sarvesh More
'''


class BankAccount:
    
    #Constructor / Initialization of class
    def __init__(self,account_holder):
        self.account_holder = account_holder
        self.balance = 0
    
    #Method to deposit money
    def deposit(self, amount):
        if(amount > 0):
            self.balance += amount
            print(f"Successfully Deposited {amount} into {self.account_holder}'s Account.")
        else:
            print(f"${amount} is not an acceptable amount")   
    
    #MEthod to withdraw money

    def withdraw(self,amount):
        if (amount > 0):
            if(amount <= self.balance):
                self.balance -= amount
                print(f"Successfully Withdrawn {amount} into {self.account_holder}'s Account.")
            else:
                print(f"Insufficient Funds in {self.account_holder}'s account")
        else:
            print(f"${amount} is not an acceptable amount")
            
            
    #method to display balance
    def display_balance(self):
        print(f"Current Balance of {self.account_holder} is {self.balance}")
