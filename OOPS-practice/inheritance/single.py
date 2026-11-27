class Animal:
    def eat(self):
        print("animal eats")

class Cat(Animal):
    def sound(self):
        print("cat meows")

c=Cat()
c.sound()
c.eat()