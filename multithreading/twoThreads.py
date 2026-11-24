import threading

def task1():
    for i in range(5):
        print("task 1")

def task2():
    for i in range(5):
        print("task 2")

t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)

t1.start()
t2.start()