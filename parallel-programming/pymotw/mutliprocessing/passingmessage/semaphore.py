import random
import multiprocessing
import time

class ActivaPool:
    def __init__(self):
        super(ActivaPool, self).__init__()
        self.mgr = multiprocessing.Manager()
        self.active = self.mgr.list()
        self.lock = multiprocessing.Lock()


    def makeActive(self, name):
        with self.lock:
            self.active.append(name)

    def makeInActive(self, name):
        with self.lock:
            self.active.remove(name)

    def __str__(self):
        with self.lock:
            return str(self.active)


def worker(s, pool):
    name = multiprocessing.current_process().name

    with s:
        pool.makeActive(name)
        print('Activating {} now running {}'.format(name, pool))
        time.sleep(random.random())
        pool.makeInActive(name)

if __name__ == '__main__':
    pool = ActivaPool()
    s = multiprocessing.Semaphore(3)
    jobs = [
        multiprocessing.Process(
            target=worker,
            name=str(i),
            args=(s,pool),
        )
        for i in range(10)
    ]
    
    for j in jobs:
        j.start()

    while True:
        alive = 0
        for j  in jobs:
            if j.is_alive():
                alive += 1
                j.join(timeout=0.1)
                print("Now running {}".format(pool))

        if alive == 0:
            break