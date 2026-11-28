import random
import datetime

class Employee:
    def __init__(self,name,doj):
        self.name=name
        self.doj=doj
        self.id=random.randrange(1,20)

    def show(self):
        print(self.name,self.doj,self.id)

    def calcDays(self):
        today=datetime.datetime.now()
        date=datetime.datetime.strptime(self.doj,"%d-%m-%Y")
        c=today-date
        print(c)


e=Employee("anna","10-10-2026")
e.show()
e.calcDays()