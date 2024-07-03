import threading
from multiprocessing import Queue

def msgSend(q):
    num = 0
    while True:
        if not q.full():
            num += 1
            rst = q.put(num)
            print("put : ", num)
            if(num==10):
                break

    print("msg Send 종료")
