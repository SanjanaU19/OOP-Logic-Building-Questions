# # Question 7 – Bank Account with Encapsulation

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount
        print("After Deposit:", self.__balance)

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("After Withdrawal:",self.__balance)
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance

b1 = BankAccount("Sanjana",5000)

print("Account Holder:", b1.name)
print("Initial Balance:", b1.get_balance())

b1.deposit(2000)
b1.withdraw(1000)

print("Current Balance:", b1.get_balance())


    