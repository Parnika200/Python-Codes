import threading
import time

def task1():
    for i in range(1,6):
        print(i)

def task2():
    k=65
    for i in range(1,6):
        print(chr(k))
        k+=1

t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()
print("main")