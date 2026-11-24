"""
join() function makes one task wait till other task completes

if you want main program to stop until a task is complete you can use join()
"""
# without join()
"""
import threading
import time

def task():
    for i in range(4):
        print("hello")
        time.sleep(1)

t=threading.Thread(target=task)
t.start()
print("main program") 
main code will execute before the task is complete
"""
#with join()
import threading
import time

def task():
    for i in range(4):
        print("hello")
        time.sleep(1)

t=threading.Thread(target=task)
t.start()
t.join()
print("main code") # main code will wait until task is executed