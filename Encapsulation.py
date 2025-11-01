# Encapsulation : 
# Wraapping data and methods inside a class
# Protects data from being directly accessed outside the class.

class BankAccount :
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance #private variable

    def deposit(self,amount):
        self.__balance+=amount
    
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient funds!")
    def get_balance(self):
        return self.__balance
acc=BankAccount("Pratik",1000)
print(acc.get_balance())
acc.deposit(500)
print(acc.get_balance())
print(acc.owner)