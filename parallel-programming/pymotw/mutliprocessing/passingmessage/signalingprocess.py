import multiprocessing
import time

def wait_for_event(e):
    print('Wait for event: Starting')
    e.wait()
    print('Wait for event: e.is_set()->', e.is_set())


def wait_for_event_timeout(e,t):
    print('Wait for event timeout: Starting')
    e.wait(t)
    print('Wait for event timeout: e.is_set()->',e.is_set())


if __name__ == '__main__':
    
    e = multiprocessing.Event()

    w1 = multiprocessing.Process(
        name='block',
        target=wait_for_event,
        args=(e,),
        )
    w1.start()

    w2 = multiprocessing.Process(
        name='nonblock',
        target=wait_for_event_timeout,
        args=(e,2),
    )
    w2.start()

    print('Main: Waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    print('Main: Event is set')


