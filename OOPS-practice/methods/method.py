"""
instance - obj specific methods self

class - class method cls @classmethod

static - exists in class,not directly connected to it @staticmethod
"""

class Student:
    def __init__(self):
        self.name="anna"
    college="IMCC"

    def show(cls):
        print(cls.college)

s=Student()
print(s.name)
s.show()