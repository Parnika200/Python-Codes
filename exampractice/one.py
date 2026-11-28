class Emp:
    def __init__(self,name,salary,dep):
        self.name=name
        self.salary=salary
        self.dep=dep

    def display(self):
        print(self.name,self.salary,self.dep)

e=Emp("anna",20000,"HR")
e.display()