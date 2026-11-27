class A:
    def __init__(self,name="unknown",age="0"):
        self.name=name
        self.age=age

a=A()
b=A("jack",20)
print(a.name,a.age)
print(b.name,b.age)
        