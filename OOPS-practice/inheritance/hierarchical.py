class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")


class Cat(Animal):

    def meow(self):
        print("Meowing")


d1 = Dog()
c1 = Cat()

d1.eat()
d1.bark()

c1.eat()
c1.meow()