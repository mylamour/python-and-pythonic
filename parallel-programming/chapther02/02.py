import threading
import time

def first():
    print(threading.current_thread().getName()+str(' is Starting\n'))

    time.sleep(3)
    print(threading.current_thread().getName()+str(' is Exiting'))

    return

def second():
    print(threading.current_thread().getName()+str(' is Starting\n'))

    time.sleep(3)
    print(threading.current_thread().getName()+str(' is Exiting'))

    return


def third():
    print(threading.current_thread().getName()+str(' is Starting\n'))

    time.sleep(3)
    print(threading.current_thread().getName()+str(' is Exiting'))

    return

if __name__ == '__main__':
    t1 = threading.Thread(name='first', target=first)
    t2 = threading.Thread(name='second', target=second)
    t3 = threading.Thread(name='third', target=third)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    