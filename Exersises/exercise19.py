#write a pthon program to define and use a class represing a bank account 

#1)create a class name bank account with the following 
#    *an attribute account_holder to store the name of the account holder
#   *an attribute balance to store the amount of money in the account intitialize to 0

#2) add the following method to the class 
#    *a method deposit to add money to the account
#    *a method withdraw to remove money from the account substract the given amount from the balance if sufficent funds exist
#    *a method display to display the account holder and the current balance

#3) write a small script to demonstrate the following
#    *create a bank account object
#    *perform a few deposits and withdrawls
#    *display the account holder and balance after each transaction


class BankAccount:
    def __init__(self,account_holder):
        self.account_holder = account_holder
        self.balance = 0
    
    def deposit(self,amount):
        if(amount>0):
            self.balance += amount
        else:
            print("Amount must be a positive number")

    def withdraw(self,amount):
        if(amount>0):
            if(self.balance >=amount):
                self.balance -= amount
            else:
                print("Insufficent funds")
        else:
            print("Amount must be a positive value")

    def display(self):
        print("Account Holder: ",self.account_holder)
        print("Account Balance: ",self.balance)



new_account = BankAccount("Sam")
new_account.display()

print()

new_account.deposit(100)
new_account.display()

print()

new_account.withdraw(-50)
new_account.display()

print()
new_account.withdraw(100)

