class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name,self.age)

class Department:
    def __init__(self,name):
        self.name=name
        self.employees=[]

    def addemp(self,emp):
        self.employees.append(emp)
        print("added emp")

    def showall(self):
        for emp in self.employees:
            emp.display()

    def search(self,emp):
        if emp not in self.employees:
            print("not found")
        else:
            print("found")

d=Department("IT")
e=Employee("anna",20)
e2=Employee("jack",21)
d.addemp(e)
d.addemp(e2)
d.showall()
d.search(e2)
        