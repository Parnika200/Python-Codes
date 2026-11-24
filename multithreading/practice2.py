import threading
import time

def study(name):
    print(name,"studying")
    time.sleep(3)

t1=threading.Thread(target=study,args=("anna",))
t2=threading.Thread(target=study,args=("jack",))
t3=threading.Thread(target=study,args=("mike",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("main code")