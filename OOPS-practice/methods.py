class A:
    def getmarks(self):
        self.a=90
        self.b=80

    def total(self):
        self.getmarks()
        print(self.a+self.b)

a=A()
a.getmarks()
a.total()