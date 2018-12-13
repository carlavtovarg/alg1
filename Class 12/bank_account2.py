class BankAccount:
    def __init__(self, ini_value = 0):
        self.__balance = int(ini_value)

    #def set__balance(self):
    #    return self.__balance
    def set_deposit(self,value):
        self.__balance = self.__balance + int(value)
    def set_withdraw(self, value):
        self.__balance = self.__balance - int(value)
    def get_balance(self):
        return self.__balance
b = BankAccount(10)
b.set_deposit(25)
b.set_withdraw(1)
print("The balance of the bank account is now " + str(b.get_balance()))