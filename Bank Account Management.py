# Question 3 – Bank Account Management

class Bank:
    def __init__(self,name,bal):
        self.name = name
        self.balance = bal

    def deposite(self,amount):
        self.balance += amount
        print("After Deposit:",self.balance)
    
    def withdraw(self,amount):
        self.balance -= amount
        print("After Withdrawal:",self.balance)

    def display_balance(self):
        print("Account Holder:",self.name)
        print("Current Balance :",self.balance)

b1 = Bank("Sanjana",5000)
print("Intital Balance : ",b1.balance)
b1.deposite(2000)
b1.withdraw(1000)
b1.display_balance()
