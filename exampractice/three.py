class Employee:
    def __init__(self,name):
        self.name=name
        self.__sal=0

    def getSal(self):
        print("salary is",self.__sal)
        if self.__sal>0:
            bonus=self.__sal*0.10
            net=self.__sal+bonus
            print("total salary",net)

    def setSal(self,sal):
        try:
            if sal<0:
                raise ValueError(">0")
            else:
                self.__sal=sal
        except ValueError as e:
            print(e)


e=Employee("anna")
e.setSal(1000)
e.getSal()