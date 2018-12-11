class BankAccount:
    balance = 0
    def __init__(self, ini_value):
        self.balance = int(ini_value)
    def deposit(self,value):
        self.balance = self.balance + int(value)
    def withdraw(self, value):
        self.balance = self.balance - int(value)
b = BankAccount(10)
b.deposit(25)
b.withdraw(1)
print("The balance of the bank account is now " + str(b.balance))