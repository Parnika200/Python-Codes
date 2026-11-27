class Parent:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)

class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age

    def display2(self):
        print(self.age)
        super().display()
    

c=Child("parnika",20)
c.display2()