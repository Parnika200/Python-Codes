class Chef:
    def cook(self):
        print("cooking")

class Waiter(Chef):
    def __init__(self):
        self.chef=Chef()

    def takeorder(self):
        print("order taken")
        self.chef.cook()

w=Waiter()
w.takeorder()
