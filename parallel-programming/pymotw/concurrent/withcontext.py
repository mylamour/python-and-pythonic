from concurrent import futures

def task(i):
    print(i)

with futures.ThreadPoolExecutor(max_workers=3) as ex:
    print('Main: Starting')
    for i in range(5):
        ex.submit(task,i)

with futures.ProcessPoolExecutor(max_workers=3) as ex:
    print('Main: Sta0rting')
    for i in range(5):
        ex.submit(task,i)

print('Main: Done')