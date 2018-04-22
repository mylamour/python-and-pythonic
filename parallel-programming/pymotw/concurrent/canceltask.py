from concurrent import futures
import time


def task(n):
    print('{}: Sleeping'.format(n))
    time.sleep(0.5)
    print('{}: Done'.format(n))
    return n / 10


def done(fn):
    if fn.cancelled():
        print('{}: Canceled'.format(fn.arg))
    elif fn.done():
        print('{}: Not canceled'.format(fn.arg))

if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=3)
    print("Main: Starting")

    tasks = []

    for i in range(10, 0, -1):
        print("Main: Submitting {}".format(i))
        f = ex.submit(task, i)
        f.arg = i
        f.add_done_callback(done)
        tasks.append((i,f))

    for i, t in reversed(tasks):
        if not t.cancel():
            print('Main: Did not cancel {}'.format(i))

    ex.shutdown()