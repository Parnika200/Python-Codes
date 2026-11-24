"""
multithreading is running several threads at same time.
thread is a small unit of execution
from multithreading module.
"""

#without multithreading
"""
def fun():
    for i in range(5):
        print("hello")

fun()
print("program finished") 
"""
# last print statement is printed after fun() is finished.


#with thread

import threading

def fun():
    for i in range(5):
     print("hello")

t=threading.Thread(target=fun) # create thread
t.start() #start thread
print("main code")