import queue
import threading
import time
q=queue.Queue()
def product(arg):
    while True:
        q.put(str(arg)+'资源')
def consumer(arg):
    while True:
        print(arg,q.get())
        time.sleep(2)
for i in range(7):
    t=threading.Thread(target=product,args=(i,))
    t.start()
for j in range(24):
    t=threading.Thread(target=consumer,args=(j,))
    t.start()