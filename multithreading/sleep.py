import threading
import time

def fun():
    for i in range(5):
        print("hello")
        time.sleep(1)

t=threading.Thread(target=fun)
t.start()