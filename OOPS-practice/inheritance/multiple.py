class Father:

    def skills1(self):
        print("Father: Programming")


class Mother:

    def skills2(self):
        print("Mother: Drawing")


class Child(Father, Mother):

    def skills3(self):
        print("Child: Dancing")


c1 = Child()

c1.skills1()
c1.skills2()
c1.skills3()