class BankAccount:

    def __init__(self, accnum, balance):
        self.__accnum = accnum
        self.__balance = float(balance)

    @property
    def accnum(self):
        return self.__accnum

    @accnum.setter
    def accnum(self, new_accnum):
        if len(str(new_accnum)) == 5:
            self.__accnum = new_accnum
        else:
            print("The account number must be 5 digits only!")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance > 0:
            self.__balance = float(new_balance)
        else:
            print("Balance must be bigger than zero or not negative!")

que = BankAccount(12345, 1000)

print(que.accnum)
print(que.balance)

que.accnum = 54321
que.balance = 2000

print(que.accnum)
print(que.balance)

que.accnum = 123
que.balance = -500
