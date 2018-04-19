import multiprocessing
import time
import sys

def daemon():
    p = multiprocessing.current_process()
    print('Starting: ',p.name, p.pid)
    time.sleep(2)
    print('Exiting: ',p.name, p.pid)
    sys.stdout.flush()

def non_daemon():
    p = multiprocessing.current_process()
    print('Starting: ',p.name, p.pid)
    time.sleep(2)
    print('Exiting: ',p.name, p.pid)
    sys.stdout.flush()


if __name__ == '__main__':

    d = multiprocessing.Process(name="Daemon", target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name="Non-Daemon", target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()

    # To wait until a process has completed it's work and exited
    # Use join() method
    # d.join()    
    # n.join()


    # Now you can try to change the time , also to comment above one
    # if timeout passed is less than the amount of time the daemon sleeps
    # the proces is still alive after join retruns

    # d.join(1)
    # print('d.is_alive(): ', d.is_alive())
    # n.join()

    