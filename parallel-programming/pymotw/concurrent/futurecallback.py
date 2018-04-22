from concurrent import futures
import time


def task(n):
    print('{}: Sleeping'.format(n))
    time.sleep(0.5)
    print('{}: Done'.format(n))

    return n/ 10

def done(fn):
    if fn.cancelled():
        print('{}: Cacnceled'.format(fn.args))
    elif fn.done():
        error = fn.exception()
        if error:
            print('{}: Error Returned: {}'.format(
                fn.args, error))

        else:
            result = fn.result()
            print('{}: Valued Returned: {}'.format(
                fn.args,
                result
            ))


if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=3)
    print('Main: Starting')

    f = ex.submit(task, 5)
    f.args = 6
    f.add_done_callback(done)
    result = f.result()
    
