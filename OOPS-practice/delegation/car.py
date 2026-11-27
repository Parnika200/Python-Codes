"""
delegation means when one class passes work to other class, manager passes work to emp

it has has-a relation
"""

class Engine:
    def start(self):
        print("engine started")

class Car(Engine):
    def __init__(self):
        self.engine=Engine()
    def drive(self):
        print("starting")
        self.engine.start()

c=Car()
c.drive()