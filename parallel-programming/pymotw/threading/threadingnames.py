import threading
import time

def worker():
    print(threading.current_thread().getName(), "Starting")
    time.sleep(0.2)
    print(threading.current_thread().getName(), "Exiting")

def services():
    print(threading.current_thread().getName(), "Starting")
    time.sleep(0.2)
    print(threading.current_thread().getName(), "Exiting")

t = threading.Thread(name='services',target=services)
w = threading.Thread(name="worker", target=worker)
w2 = threading.Thread(target=worker)

w.start()
w2.start()
t.start()
