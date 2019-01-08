class BankAccount:

    def __init__(self, account_number):

        self.__balance = 0
        self.__account_number = account_number

    #mutator
    def set_balance(self, balance: float):
        self.__balance = balance


    def get_balance(self):
        return self.__balance

    def set_acc_num(self, account_number):
        self.__account_number = account_number

    def get_acc_num(self):
        return self.__account_number