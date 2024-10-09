from bankAccount import *

if __name__ == "__main__":
    sarvesh = BankAccount("Sarvesh")
    
    sarvesh.deposit(20)
    sarvesh.withdraw(10)
    sarvesh.deposit(50)
    sarvesh.withdraw(40)
    sarvesh.display_balance()
    
