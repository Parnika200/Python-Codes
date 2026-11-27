class A:
    def __init__(self,num):
        self.num=num

    def __add__(self,other):
        print(self.num+other.num)

    def __sub__(self,other):
        print(self.num-other.num)

    def __mul__(self, other):
         print(self.num*other.num)

    def __eq__(self,other):
        return self.num==other.num

    def __gt__(self, other):
        return self.num>other.num

a=A(20)
b=A(90)
a+b
a-b
a*b
print(a==b)
print(a>b) 