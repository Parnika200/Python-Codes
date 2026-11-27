class A:
    def __init__(self):
        print("obj created")
    def __del__(self):
        print("obj deleted")

a=A()
del a