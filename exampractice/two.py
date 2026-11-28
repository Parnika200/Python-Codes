class Product:
    def __init__(self,name):
        self.name=name
        self.__price=0

    def getP(self):
        print(self.__price)

    def setP(self,p):
        try:
            if p<0:
                raise ValueError("price cannot be <0")
            else:
                self.__price=p
        except ValueError as e:
            print(e)

    def display(self):
        print(self.name)

p=Product("dress")
p.display()
p.setP(-1)
p.getP()
            