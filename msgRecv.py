import threading
from multiprocessing import Queue

def msgRecv(q):
    while True:
        if not q.empty():
            rst = q.get()
            print("get : ", rst)
            if(rst==10):
                break
        
    print("msg Recv 종료")