class Student:
    def __init__(self,name,email,age):
        try:         
            if "@" not in email:
                raise ValueError("email wrong")
            elif age<0:
                raise ValueError("wrong age")
            else:
                self.name=name
                self.email=email
                self.age=age
        except ValueError as e:
            print(e)

    def display(self):
        print(self.name,self.email,self.age)

s=Student("anna","agmail.com",20)
   

        