import threading
import time

def task1():
    for i in range(3):
        print("task 1")
        time.sleep(1)

def task2():
    for i in range(3):
        print("task 2")
        time.sleep(2)

t1=threading.Thread(target=task1)
t1.start()
t1.join()
t2=threading.Thread(target=task2)
t2.start()
t2.join()
print("main code")

# task2 will wait until task1 is complete, main will wait until task2 is complete