class Grandma():
    def skill1(self):
        print("cooking")

class Mom(Grandma):
    def skill2(self):
        print("baking")

class Child(Mom):
    def skill3(self):
        print("dancing")

c=Child()
c.skill1()
c.skill2()
c.skill3()