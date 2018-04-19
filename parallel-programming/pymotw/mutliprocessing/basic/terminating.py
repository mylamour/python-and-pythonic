import multiprocessing
import time

def slow():
    print("Starting ...")
    time.sleep(1)
    print("Exiting ...")


if __name__ == '__main__':
    p = multiprocessing.Process(target=slow)
    print("Before: ", p, p.is_alive())

    p.start()
    print("Start: ", p, p.is_alive())

    p.terminate()
    print("Terminated: ", p, p.is_alive())

    p.join()
    print("Joined: ", p, p.is_alive())
            
    