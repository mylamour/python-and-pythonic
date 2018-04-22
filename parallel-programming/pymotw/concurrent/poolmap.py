from concurrent import futures
import threading
import time

def task(n):
    print('{}: sleeping {}'.format(
        threading.current_thread().name,
        n
    ))

    time.sleep(n /10)

    print('{}: done with {}'.format(
        threading.current_thread().name,
        n
    ))

    return n/10


ex = futures.ThreadPoolExecutor(max_workers=4)

print('Main: Starting')

resluts = ex.map(task, range(5,0,-1))

print('Main: Unprocessed Results {}'.format(resluts))
print('Main: Waiting for Real Results')

realresults= list(resluts)
print('Main: Results {}'.format(realresults))