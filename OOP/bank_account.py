import time


class BankAccount(object):
    count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = BankAccount.count
        self.showBalance()
        self.transaction = []
        BankAccount.count += 1

    def withdraw(self, total):
        if total > self.balance:
            print(f"Your balance is {self.balance}. You don't have enough money to withdraw that amount")
        else:
            self.balance -= total
            print(f"You withdrew {total} and your balance is now {self.balance}")
            self.showBalance()
            self.transaction_histry(total, "withdraw")

    def deposit(self, total):
        self.balance += total
        print(f"Your balance has been updated. Your balance is {self.balance} now")
        self.showBalance()
        self.transaction_histry(total, "deposit")

    def showBalance(self):
        print(f"{self.name}(口座番号：{self.account_number})の残高は{self.balance}円です")

    def transaction_histry(self, total, type):
        if type == "withdraw":
            self.transaction.append({"Name" : self.name, "Balance" : self.balance, "Withdraw": total, "Time": BankAccount.get_time()})
        elif type == "deposit":
            self.transaction.append({"Name": self.name, "Balance": self.balance, "Deposit": total, "Time": BankAccount.get_time()})
        print(self.transaction)

    @staticmethod
    def get_time():
        current_time = time.localtime()
        return "{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分".format(current_time)


john = BankAccount("John", 1000000)
print(john.account_number)
john.withdraw(10000)

mac = BankAccount("Mac", 2121)
print(mac.account_number)
mac.deposit(2123)
mac.deposit(2123)
print(BankAccount.get_time())