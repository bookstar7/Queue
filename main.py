import threading
from multiprocessing import Queue
from msgSend import *
from msgRecv import *
import time

q = Queue()

t1 = threading.Thread(target=msgSend, args=(q,))
t2 = threading.Thread(target=msgRecv, args=(q,))

t1.start()
t2.start()

t1.join()
t2.join()

print("main exit")