class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def show(self):
        print(self.name,self.price)

class Custome(Exception):
    pass

try:
    n=int(input("enter price"))
    name=input("name")
    if n<=0:
        raise Custome("price must be >0")
    else:
      p=Product(name,n)
except Custome as e:
    print(e)
