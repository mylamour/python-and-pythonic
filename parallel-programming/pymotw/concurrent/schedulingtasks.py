from concurrent import futures
import threading
import time


def task(n):
    print('{}: sleeping {}'.format(
        threading.current_thread().name,
        n
    ))

    time.sleep(n)

    print('{}: done with {}'.format(
        threading.current_thread().name,
        n
    ))


ex = futures.ThreadPoolExecutor(max_workers=2)

print('Main: Starting')

f = ex.submit(task, 5)


print('Main: Future: {}'.format(f))
print('Main: Waiting for results')

result = f.result()

print('Main: Result: {}'.format(result))
print('Main: Future After Result: {}'.format(f))

wait_for = [
    ex.submit(task,i) 
    for i in range(5,0,-1)
]

for f in futures.as_completed(wait_for):
    print('Main: Result: {}'.format(f.result()))

