import multiprocessing
import pprint

def worker(d, k ,v):
    d[k] = v

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    d = mgr.dict()

    jobs = [
        multiprocessing.Process(
            target=worker,
            args=(d, i, i*2),
        )
        for i in range(10)
    ]
    

    for j in jobs:
        j.start()
    for j in jobs:
        j.join()

    print('Results: ', d)
    