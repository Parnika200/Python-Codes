"""
multithreading is running several threads at same time.
thread is a small unit of execution
from multithreading module.

multithreading / asyncio

multithreading uses multiple threads, os decides which threads to use
asyncio uses single event loop and coroutines. control switched manually

Advantages
Responsiveness: the app never appears frozen during slow operations.
Better use of waiting time: I/O-bound work speeds up dramatically because one thread's wait is another thread's work time.
Shared memory: threads in the same process share data directly, so communication is cheap compared to separate processes.
Lightweight compared to processes: creating and switching threads costs less than starting new processes.
True parallelism on multiple cores: in languages without a GIL (Java, C++, Go, C#), threads can run on different CPU cores simultaneously, speeding up CPU-heavy work too.
Simpler mental model for blocking code: you can write ordinary sequential code in each thread instead of restructuring everything around async/await.
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