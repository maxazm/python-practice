class Account:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, price):
        self.__balance += price
        self.show_balance()

    def withdraw(self, price):
        if self.__balance < price:
            print("残高が足りません")
            self.show_balance()
        else:
            self.__balance -= price
            self.show_balance()

    def show_balance(self):
        print(f"残高は{self.__balance}円です")

myaccount = Account(10000)
print(dir(myaccount))
myaccount.deposit(1000)
myaccount.withdraw(100)
myaccount.deposit = 1000
myaccount.__balance = -10000
print(myaccount.__balance)
myaccount.show_balance()
print(dir(myaccount))
