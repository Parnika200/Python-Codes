import threading
import time

def download(name):
    print(name,"downloading.....")
    time.sleep(4)
    print(name,"completed")

t1=threading.Thread(target=download,args=("file 1",))
t2=threading.Thread(target=download,args=("file 2",))
t3=threading.Thread(target=download,args=("file 3",))

t1.start()
t1.join()
t2.start()
t2.join()
t3.start()
t3.join()



print("main code")