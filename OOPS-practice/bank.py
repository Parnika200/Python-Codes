class Custom(Exception):
    pass

class Bank:
    def __init__(self,name):
        self.__balance=9000
        self.name=name

    def withdraw(self,amt):
        try:
            if amt>self.__balance:
                raise Custom("amt > balance")
            else:
                self.__balance-=amt
        except Custom as e:
            print(e)

    def deposit(self,amt):
        try:
            if amt<0:
                raise Custom("amount cannot be <0")
            else:
                self.__balance+=amt
        except Custom as e:
            print(e)

    def getBal(self):
        print("balance is",self.__balance)

b=Bank("IDBI")

b.getBal()
b.withdraw(80)
b.getBal()
b.deposit(1000)
b.getBal()

        
