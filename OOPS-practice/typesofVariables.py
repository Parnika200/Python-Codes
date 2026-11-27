"""
instance variable - unique for each obj
class variable - common for all obj
private - __name, cannot be directly accessed, name mangling is used
protected - _name, accessed only by class and subclass
"""

class Student:
    college="IMCC"

    def __init__(self,name,m):
        self.name=name
        self.__marks=m

    def getMarks(self):
        print(self.__marks)



s=Student("anna",90)
s1=Student("jack",80)
s.college="MES"
print(s.name,s.college)
s.getMarks()
print(s1.name,s1.college)
print(Student.college)